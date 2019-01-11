# keras-yolo3-Mobilenet

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction

A Keras implementation of YOLOv3 (Tensorflow backend) inspired by [allanzelener/YAD2K](https://github.com/allanzelener/YAD2K).
#### And I change the backend of darknet53 into Mobilenet

# Guide of keras-yolov3-Mobilenet

1.train_Mobilenet.py 
     
     Code for training
     (I change some of the code to read in train.txt and val.txt seperately, remember to change that, and the .txt file are in the same form descibed below)

2.yolo3/model_Mobilenet.py 
    
    model_Mobilenet is the yolo model based on Mobilenet
    ##### If you want to go through the source code,ignore the other function,please see the yolo_body ####
    (I extract three layers from the Mobilenet to make the prediction)

3.yolo_image.py and yolo_class.py
    
    use yolo_image to test and evaluate the image and video. yolo_class define the YOLO class.

4. coco_annotation.py

    convert COCO .json file into .txt for training
 
5. voc_annotation.py
    
    convert VOC .xml file into .txt for training
    


