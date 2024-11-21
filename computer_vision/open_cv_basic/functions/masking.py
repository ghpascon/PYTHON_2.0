import cv2 as cv
import numpy as np
from functions import show, draw, bitwise, basics

def get_mask(mask_shape, obj, blank):
    if mask_shape == 0:
        mask = draw.draw_rectangles(
            img_path=blank,
            rects=obj,
            color=(255, 255, 255)
            )
    elif mask_shape ==1:
        mask = draw.draw_circles(
            img_path=blank,
            circles=obj,
            color=(255, 255, 255)
            )  
    elif mask_shape ==2:  
        mask = draw.draw_lines(
            img_path=blank,
            lines=obj,
            color=(255, 255, 255)
            )     
    elif mask_shape ==3:
        mask = draw.draw_words(
            img_path=blank,
            words=obj,
            color=(255, 255, 255)
            )   
    return mask

def mask(img_path, mask_shape, obj):
    """
    mask_shape: 
    0 -> rectangle
    1 -> circle
    2 -> line
    3 -> word
    """
    if isinstance(img_path, str):
        img = cv.imread(img_path)
    else:
        img = img_path    

    blank = draw.draw_blank_img(width=img.shape[1], height=img.shape[0])

    mask = get_mask(mask_shape, obj, blank)

    masked = cv.bitwise_and(img,mask)
    return masked