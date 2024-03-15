import os
import random
import shutil


def divide_dataset(path, o_path, train_p, val_p):
    print('正在拆分数据集......')
    shutil.rmtree(o_path, ignore_errors=True)
    train_path = os.path.join(o_path, 'train')
    train_path_i = os.path.join(train_path, 'images')
    train_path_l = os.path.join(train_path, 'labels')
    val_path = os.path.join(o_path, 'val')
    val_path_i = os.path.join(val_path, 'images')
    val_path_l = os.path.join(val_path, 'labels')

    os.mkdir(o_path)
    os.mkdir(train_path)
    os.mkdir(train_path_i)
    os.mkdir(train_path_l)
    os.mkdir(val_path)
    os.mkdir(val_path_i)
    os.mkdir(val_path_l)

    image_dir = os.path.join(path, 'images')
    txt_dir = os.path.join(path, 'labels')
    dir_list = list(os.listdir(image_dir))
    true_list = []
    background_list = []
    for filename in dir_list:
        txt_filename = f'{os.path.splitext(filename)[0]}.txt'
        img_path = os.path.join(image_dir, filename)
        txt_path = os.path.join(txt_dir, txt_filename)
        if not os.path.exists(txt_path):
            background_list.append(filename)
            shutil.copy(img_path, train_path_i)
        else:
            true_list.append(filename)

    n = len(true_list)
    random.shuffle(true_list)
    train_list = true_list[:int(n * train_p / 10)]
    val_list = true_list[int(n * train_p / 10):]

    for filename in train_list:
        txt_filename = f'{os.path.splitext(filename)[0]}.txt'
        txt_path = os.path.join(txt_dir, txt_filename)
        img_path = os.path.join(image_dir, filename)
        shutil.copy(img_path, train_path_i)
        shutil.copy(txt_path, train_path_l)

    for filename in val_list:
        txt_filename = f'{os.path.splitext(filename)[0]}.txt'
        txt_path = os.path.join(txt_dir, txt_filename)
        img_path = os.path.join(image_dir, filename)
        shutil.copy(img_path, val_path_i)
        shutil.copy(txt_path, val_path_l)
    print('拆分完毕！')


divide_dataset('data/i_datasets', 'data/datasets', 8, 2)
