import cv2 as cv
from functions import show,basics

def main():
    show.show_image(basics.normalized_img("Photos/cat.jpg", 1))
    show.show_image(basics.normalized_img("Photos/cat.jpg", 2))
    show.show_image(basics.normalized_img("Photos/cat.jpg", 3))
    show.show_image(basics.normalized_img("Photos/cat.jpg", 4))
    show.show_image(basics.normalized_img("Photos/cat.jpg", 5))

    img=basics.scale_img("Photos/cat.jpg", 1.5)
    show.show_image(basics.normalized_img(img, 5))

    img_resized=basics.resize_img(frame="Photos/cat.jpg", dimensions=(500,300))
    show.show_image(basics.normalized_img(img_resized, 5))
    
    show.show_image("Photos/cat.jpg")
    normalized_img = basics.normalized_img("Photos/cat.jpg", 5)
    img_countour = basics.get_contour_img(normalized_img)
    show.show_image(img_countour)

if __name__=="__main__":
    main()
