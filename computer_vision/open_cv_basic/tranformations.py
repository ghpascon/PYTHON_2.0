import cv2 as cv
from functions import show, tranformations

def main():
    show.show_image(img_adress="Photos/cat.jpg")
    show.show_image(tranformations.translate_img("Photos/cat.jpg", 100, 100))
    show.show_image(tranformations.rotate_img("Photos/cat.jpg", 90))
    show.show_image(tranformations.flip_img("Photos/cat.jpg", -1))
    show.show_image(tranformations.crop_img("Photos/cat.jpg", 200, 200, 300, 200))

if __name__=="__main__":
    main()
