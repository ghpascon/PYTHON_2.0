import cv2 as cv
from functions import color_img, show

def main():
    show.show_image("Photos/park.jpg")
    show.show_image(color_img.color_converter("Photos/park.jpg", code=cv.COLOR_BGR2GRAY))
    show.show_image(color_img.grayscale_img("Photos/park.jpg"))
    show.show_image(color_img.hsv_img("Photos/park.jpg"))
    show.show_image(color_img.lab_img("Photos/park.jpg"))
    show.show_image(color_img.rgb_img("Photos/park.jpg"))
    img_b,img_g,img_r=color_img.split_colors("Photos/park.jpg")
    show.show_image(img_b, "Blue")
    show.show_image(img_g, "Green")
    show.show_image(img_r, "Red")

    merge_img=color_img.merge_colors(img_b,img_g,img_r)
    show.show_image(merge_img, "Merge")

if __name__=="__main__":
    main()
