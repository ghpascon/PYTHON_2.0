import cv2 as cv
from functions import show, draw, masking, basics, bitwise

def main():
    #basic masking
    img = basics.get_img("Photos/cats.jpg")
    blank = draw.draw_blank_img(width=img.shape[1],height=img.shape[0])
    circulos=(
        ((300,170),150,cv.FILLED),
        )  
    mask = draw.draw_circles(
    img_path=blank,
    circles=circulos,
    color=(255, 255, 255)
    )

    masked = bitwise.bitwise_and(img, mask)
    show.show_image(masked)

    #use function masking
    retangulos=(
        ((200,100),(400,400),cv.FILLED), 
        )    
    circulos=(
        ((300,300),150,cv.FILLED),
        )    
    lines=(
        ((100,100),(100,50),20), 
        ((0,300),(300,300),30), 
        ((300,200),(500,400),50)
        )
    words=(
        ("Hello", (100,100), cv.FONT_HERSHEY_TRIPLEX, 1.0, 2), 
        ("World", (200,200), cv.FONT_HERSHEY_DUPLEX, 1.5, 5), 
        ("Test", (300,400), cv.FONT_HERSHEY_SIMPLEX, 3.0, 10), 
        )

    masked_img = masking.mask(img_path="Photos/cats.jpg", mask_shape=0, obj=retangulos)
    show.show_image(masked_img)  

    masked_img = masking.mask(img_path="Photos/cats.jpg", mask_shape=1, obj=circulos)
    show.show_image(masked_img)  

    masked_img = masking.mask(img_path="Photos/cats.jpg", mask_shape=2, obj=lines)
    show.show_image(masked_img)  

    masked_img = masking.mask(img_path="Photos/cats.jpg", mask_shape=3, obj=words)
    show.show_image(masked_img)      


if __name__ == "__main__":
    main()


