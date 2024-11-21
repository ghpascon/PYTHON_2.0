import cv2 as cv
import numpy as np
from functions import basics

def show_image(img_adress=None, name='IMG', scale=1):
    """
    img_adress -> the path to the image.
    name -> the name that will show on the window.
    scale -> set the scale.
    """
    if isinstance(img_adress, str):
        img = cv.imread(img_adress)
    else:
        img = img_adress

    if(scale!=1):
        img=basics.scale_img(img, scale)
    cv.imshow(name, img)
    cv.waitKey(0)

def show_video(video=None, name='Video', scale=1):
    """
    video -> 0,1,2,... the camera connected or pass the file path.
    name -> the name that will show on the window.
    scale -> set the scale.
    press 'd' to destroy window
    """
    capture = cv.VideoCapture(video)

    while(True):
        isTrue, frame = capture.read()
        if(scale!=1):
            frame=basics.scale_img(frame, scale)

        cv.imshow(name, frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    
    capture.release()
    cv.destroyAllWindows()

