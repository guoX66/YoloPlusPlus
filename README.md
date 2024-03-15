# YoloPlusPlus   (Updating)

## using Yolov8 head, modify its backbone with Resnext50_32dx4 and Unet++ structure



## Environment

please make sure the pytorch_cuda and ultralytics and pytorch_cuda environments are set up

You can execute the following commands on the command line in order



if cuda>=11.8

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

For other versions, you can check the [PyTorch](https://pytorch.org/get-started/locally/) website for the download command



Then install the ultralytics dependency

```bash
pip install ultralytics
```

Or you can go to the [website](https://github.com/ultralytics/ultralytics)  to find specific dependencies, this project has modified some of its content and put it inside the project. When the training program is run in this project, it is automatically conducted from the ultralytics in this project.



## Quick start

Put the data in the data folder
If you haven't done a train-validation split yet, you can store datasets of YOLO format in images and labels under data/_i_datasets



run the divide script

```bash
python divide.py
```



then run the train script 

```
python train.py
```


