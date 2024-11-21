import cv2 as cv
from functions import show

def main():
    show.show_video('Videos/dog.mp4')
    show.show_video(0,'Webcam')
    show.show_video(0,'Webcam', 1.5)

if __name__=="__main__":
    main()
