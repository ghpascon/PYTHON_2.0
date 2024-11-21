import cv2 as cv
from functions import show,basics

def main():
    img = "Photos/cats.jpg"
    normalized_img = basics.normalized_img(img, 2)
    adaptive_tresh = basics.thresholding(normalized_img)
    treshold_img = basics.thresholding(normalized_img, min_value=100)
    inv_treshold_img = basics.thresholding(normalized_img, min_value=100, inverse=True)
    show.show_image(img)
    show.show_image(adaptive_tresh)
    show.show_image(treshold_img)
    show.show_image(inv_treshold_img)

if __name__=="__main__":
    main()
