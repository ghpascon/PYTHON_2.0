import cv2 as cv
from functions import show,basics

def main():
    img = "Photos/park.jpg"
    normalized_img = basics.normalized_img(img, 1)
    show.show_image(basics.edge_img(img_path=normalized_img,mode=0))
    show.show_image(basics.edge_img(img_path=normalized_img,mode=1))
    show.show_image(basics.edge_img(img_path=normalized_img,mode=2))
    show.show_image(basics.edge_img(img_path=normalized_img,mode=3))
    show.show_image(basics.edge_img(img_path=normalized_img,mode=4))

if __name__=="__main__":
    main()
