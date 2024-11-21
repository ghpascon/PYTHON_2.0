import cv2 as cv
from functions import show, draw, bitwise


def main():
    blank=draw.draw_blank_img(width=500, height=500)
    show.show_image(blank)

    #retangulos
    retangulos=(
        ((200,200),(400,400),cv.FILLED),
        )

    rectangles = draw.draw_rectangles(
    img_path=blank.copy(),
    rects=retangulos,
    color=(255, 0, 0)
    )

    show.show_image(rectangles)

    #draw circles
    circulos=(
        ((250,250),150,cv.FILLED),
        )

    circles = draw.draw_circles(
    img_path=blank.copy(),
    circles=circulos,
    name='circles',
    color=(255, 0, 0)
    )

    show.show_image(circles)

    show.show_image(bitwise.bitwise_and(rectangles, circles))
    show.show_image(bitwise.bitwise_or(rectangles, circles))
    show.show_image(bitwise.bitwise_xor(rectangles, circles))
    show.show_image(bitwise.bitwise_not(rectangles))



if __name__=="__main__":
    main()
