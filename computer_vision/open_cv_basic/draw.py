import cv2 as cv
from functions import draw

def main():
    #blank img
    draw.draw_blank_img(700, 500, 'Blank', color=(0,0,255),get=False)

    #draw rectangles
    retangulos=(
        ((0,0),(100,100),2), 
        ((200,300),(450,450),8), 
        ((300,50),(450,200),cv.FILLED)
        )

    draw.draw_rectangles(
    img_path="Photos/cat.jpg",
    rects=retangulos,
    name='Rectangles',
    color=(255, 0, 0),  # Cor vermelha em RGB
    get=False
    )

    #draw circles
    circulos=(
        ((100,100),10,2), 
        ((200,300),15,8), 
        ((300,50),20,cv.FILLED)
        )

    draw.draw_circles(
    width=700,
    height=500,
    circles=circulos,
    name='circles',
    color=(255, 250, 0),
    get=False
    )
    
    #draw lines
    lines=(
        ((100,100),(100,50),2), 
        ((0,300),(300,300),8), 
        ((300,200),(500,400),5)
        )

    draw.draw_lines(
    img_path="Photos/park.jpg",
    lines=lines,
    name='Lines',
    color=(255, 255, 255),
    get=False
    )

    #draw words
    words=(
        ("Hello", (100,100), cv.FONT_HERSHEY_TRIPLEX, 1.0, 2), 
        ("World", (200,200), cv.FONT_HERSHEY_DUPLEX, 1.5, 5), 
        ("Test", (300,400), cv.FONT_HERSHEY_SIMPLEX, 3.0, 10), 
        )

    draw.draw_words(
    width=700,
    height=500,
    words=words,
    name='Words',
    color=(255, 255, 255),
    get=False
    )

if __name__=="__main__":
    main()
