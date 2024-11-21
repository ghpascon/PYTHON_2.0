import cv2 as cv
from functions import haarcascade_detection, show, draw, basics

def main():
    people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
    
    img_path="Faces/val/elton_john/1.jpg"

    haarcascade_path = "haarcascades/haarcascade_frontalface_default.xml"

    model_path = "train_model/face_trained.yml"

    img = haarcascade_detection.recognizer(
        img_path=img_path,
        haar_cascade_path=haarcascade_path,
        model_path=model_path,
        obj=people,
        scaleFactor=1.1,
        minNeighbors=1,
        min_distance=50
        )
    
    show.show_image(img)

if __name__ == "__main__":
    main()



