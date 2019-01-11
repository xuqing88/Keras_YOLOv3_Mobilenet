import sys
from yolo_class import YOLO, detect_video
from PIL import Image
import os
import cv2

def detect_img(img,yolo):
    r_image = yolo.detect_image(img)
    return r_image

if __name__ == '__main__':
    # class YOLO defines the default value
    yolo = YOLO()
    FLAG = False
    if FLAG is True:
        for (root, dirs, files) in os.walk('images/test'):
            if files:
                for f in files:
                    print(f)
                    path = os.path.join(root, f)
                    image = Image.open(path)
                    image = detect_img(image, yolo)
                    image.save('images/res/'+f)
        yolo.close_session()
    else:
        video_path = "videos/test/road_mobilenet.mp4"
        video_save_path = "videos/res/road_mobilenet_score_0.5.mp4"
        detect_video(yolo, video_path, video_save_path)
