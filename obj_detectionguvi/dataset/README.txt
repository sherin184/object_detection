# Object Detection using YOLOv8

## Overview

This project implements an **Object Detection System** using the **YOLOv8** deep learning model. It detects multiple objects from **images, videos, and live webcam streams** using a pretrained YOLOv8 model. The application is built with **Python**, **OpenCV**, and the **Ultralytics YOLOv8** library.

## Features

* Real-time object detection using a webcam
* Object detection from images
* Object detection from videos
* Uses pretrained **YOLOv8m** model
* Displays bounding boxes, class labels, and confidence scores
* Simple menu-driven interface

## Technologies Useds

* Python 3.x
* yolov8m (Ultralytics)
* OpenCV


## Project Structure

text
ObjectDetection/
│── detect.py
│── requirements.txt
│── yolov8m.pt
```



## Installation

Install the required libraries:

bash
pip install ultralytics opencv-python matplotlib
```


## Run the Project

bash
python detect.py
```

Choose one of the following options:

* **1** – Webcam Detection
* **2** – Image Detection
* **3** – Video Detection


## Output

The application detects objects and displays:

* Bounding boxes
* Object class names
* Confidence scores

Press **Q** to exit webcam or video detection.



## Conclusion

This project demonstrates real-time object detection using the pretrained YOLOv8 model. It provides an easy way to detect objects from images, videos, and webcams, making it suitable for learning computer vision and object detection concepts.
