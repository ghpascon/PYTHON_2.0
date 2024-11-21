import cv2 as cv
from functions import haarcascade_detection, show,draw,basics

def lady():
    img = "Photos/lady.jpg"
    normalized_img = basics.normalized_img(img, 1)
    haarcascade_path = "haarcascades/haarcascade_frontalface_default.xml"
    
    faces_rects = haarcascade_detection.haarcascade_detection(
        normalized_img, 
        haarcascade_path, 
        scaleFactor=1.1,
        minNeighbors=5,
        min_distance=50
        )

    print(f'Faces found: {len(faces_rects)}')

    retangulos = haarcascade_detection.get_rect(faces_rects)

    rect_img = draw.draw_rectangles(
    img_path=img,
    rects=retangulos,
    name='Rectangles',
    color=(255, 0, 0)  
    )

    show.show_image(rect_img)

def group_1():
    img = "Photos/group 1.jpg"
    normalized_img = basics.normalized_img(img, 1)
    haarcascade_path = "haarcascades/haarcascade_frontalface_default.xml"
    
    faces_rects = haarcascade_detection.haarcascade_detection(
        normalized_img, 
        haarcascade_path, 
        scaleFactor=1.1,
        minNeighbors=1,
        min_distance=10
        )

    print(f'Faces found: {len(faces_rects)}')

    retangulos = haarcascade_detection.get_rect(faces_rects)

    rect_img = draw.draw_rectangles(
    img_path=img,
    rects=retangulos,
    name='Rectangles',
    color=(255, 0, 0)  
    )

    show.show_image(rect_img)

def group_2():
    img = "Photos/group 2.jpg"
    normalized_img = basics.normalized_img(img, 1)
    haarcascade_path = "haarcascades/haarcascade_frontalface_default.xml"
    
    faces_rects = haarcascade_detection.haarcascade_detection(
        normalized_img, 
        haarcascade_path, 
        scaleFactor=1.1,
        minNeighbors=5,
        min_distance=50
        )

    print(f'Faces found: {len(faces_rects)}')

    retangulos = haarcascade_detection.get_rect(faces_rects)

    rect_img = draw.draw_rectangles(
    img_path=img,
    rects=retangulos,
    name='Rectangles',
    color=(255, 0, 0)  
    )

    show.show_image(rect_img)

def video():
    haarcascade_path = "haarcascades/haarcascade_frontalface_default.xml"
    haarcascade_detection.video_haarcascade_detection(
    0, 
    haar_cascade_path=haarcascade_path, 
    scaleFactor=1.1,
    minNeighbors=5,
    min_distance=200,
    name="Web Cam detector"
    )

def main():
    # lady()
    # group_1()
    # group_2()
    video()

if __name__=="__main__":
    main()
