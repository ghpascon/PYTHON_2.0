import cv2 as cv
from functions import haarcascade_detection, show, draw, basics

def main():
    img_path = [
        'Faces/train/Ben Afflek', 
        'Faces/train/Elton John', 
        'Faces/train/Jerry Seinfield', 
        'Faces/train/Madonna', 
        'Faces/train/Mindy Kaling'
    ]
    
    haarcascade_path = "haarcascades/haarcascade_frontalface_default.xml"

    haarcascade_detection.create_train(
        paths=img_path,
        haar_cascade_path=haarcascade_path, 
        scaleFactor=1.1,
        minNeighbors=1,
        min_distance=50
    )
    
if __name__ == "__main__":
    main()
