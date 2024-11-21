import cv2 as cv
from functions import show

def main():
    show.show_image(img_adress='Photos/cat.jpg')
    show.show_image(img_adress='Photos/cats.jpg',name='cats')
    show.show_image(img_adress='Photos/cats.jpg',name='cats',scale=2)

if __name__=="__main__":
    main()
