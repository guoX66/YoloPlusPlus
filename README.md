# YoloPlusPlus   (Updating)

## using Yolov8 head, modify its backbone with Resnext50_32dx4 and Unet++ structure

### The project implementation is mainly in the submodule [simple_YOLO](https://github.com/guoX66/simple_YOLO)

 

## Pull

Pull down the submodules as well with git:

```bash
git clone --recurse-submodules https://github.com/guoX66/YoloPlusPlus.git
```

Or download sub-projects and put them into this project



## Environment

Please refer to the subproject introduction for environment configuration.



## Quick start

This project uses timm to implement Resnext50_32dx4. If you cannot ensure that the pre-trained model downloaded, please download the pre-trained model from release and put it into predict_weights



Then go to the simple_YOLO folder to train, test, etc

```bash
cd simple_YOLO
```


