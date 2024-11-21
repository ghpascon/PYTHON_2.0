import cv2 as cv
import numpy as np
from functions import basics, obj_detection

def show_image(img_adress=None, name='IMG', scale=1, object_detection=False, model=None, min_confidence=50, detection_area=None):
    """
    img_adress -> the path to the image.
    name -> the name that will show on the window.
    scale -> set the scale.
    """
    if isinstance(img_adress, str):
        img = cv.imread(img_adress)
    else:
        img = img_adress

    if scale != 1:
        img = basics.scale_img(img, scale)

    if object_detection:
        # Detectar objetos e filtrar pela área de detecção
        objects = obj_detection.detect_objects(img, model, confidence_threshold=min_confidence, detection_area=detection_area)
        
        # Desenhar as caixas e rótulos na imagem
        for obj in objects:
            x_min, y_min, x_max, y_max = obj['coordinates']
            label = obj['label']
            # Desenhar o retângulo
            cv.rectangle(img, (x_min, y_min), (x_max, y_max), color=(0, 255, 0), thickness=2)
            # Adicionar o texto do rótulo
            cv.putText(img, label, (x_min, y_min - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        if detection_area is not None:
            (x_min_area, y_min_area), (x_max_area, y_max_area) = detection_area
            cv.rectangle(img, (x_min_area, y_min_area), (x_max_area, y_max_area), (0, 0, 255), 3)

    cv.imshow(name, img)
    cv.waitKey(0)

def show_video(video=None, name='Video', scale=1, object_detection=False, model=None, frames=50, min_confidence=50, detection_area=None):
    """
    video -> 0,1,2,... the camera connected or pass the file path.
    name -> the name that will show on the window.
    scale -> set the scale.
    press 'd' to destroy window
    """
    frame_count = 0
    capture = cv.VideoCapture(video)
    objects = []

    while True:
        isTrue, frame = capture.read()
        if not isTrue:
            break  # Break if there are no more frames to read

        if scale != 1:
            frame = basics.scale_img(frame, scale)

        # Realizar a detecção de objetos em intervalos de quadros definidos
        if object_detection:
            if frame_count % frames == 0:
                objects = obj_detection.detect_objects(frame, model, confidence_threshold=min_confidence, detection_area=detection_area)
        
            # Desenhar as caixas e rótulos na imagem
            for obj in objects:
                x_min, y_min, x_max, y_max = obj['coordinates']
                label = obj['label']
                # Desenhar o retângulo
                cv.rectangle(frame, (x_min, y_min), (x_max, y_max), color=(0, 255, 0), thickness=2)
                # Adicionar o texto do rótulo
                cv.putText(frame, label, (x_min, y_min - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            if detection_area is not None:
                (x_min_area, y_min_area), (x_max_area, y_max_area) = detection_area
                cv.rectangle(frame, (x_min_area, y_min_area), (x_max_area, y_max_area), (0, 0, 255), 3)

        cv.imshow(name, frame)

        # Break the loop if 'd' key is pressed
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

        frame_count += 1  # Increment the frame counter

    capture.release()
    cv.destroyAllWindows()
