import json
import os
import yaml
import sys
import platform
import torch

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,current_dir)

from ultralytics import YOLO

def make_yaml(curpath, train_data, class_dict):
    desired_caps = {
        'path': f'{curpath}/data/datasets',  # dataset root dir
        'train': 'train/images',
        'val': 'val/images',
        # Classes
        'names': class_dict

    }
    with open(train_data, "w", encoding="utf-8") as f:
        yaml.dump(desired_caps, f)

        
class_dict = {0: 'hand'}

os_name = str(platform.system())
if os_name == 'Windows':
    num_workers = 0
else:
    num_workers = 32
if torch.cuda.is_available():
    gpu_num = torch.cuda.device_count()
    device = [i for i in range(gpu_num)]
else:
    device = torch.device('cpu')
    
batch=40 if device==[0] else 160
print(f'device : {device}')
print(f'batch : {batch}')

make_yaml(current_dir, 'Cfg.yaml', class_dict)
path = 'models/yolov8l-resnext50.yaml'
model = YOLO(path, verbose=True)
results = model.train(
        data='Cfg.yaml',
        epochs=50,
        workers=num_workers,
        batch=2,
        device=device,
        amp=True

    )
