from functions import show
import torch

def main():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    img_path = "Photos/carros_2.png"
    show.show_image(img_path, object_detection=True, model=model,  min_confidence=50)

    detection_area= ((10,200),(950,600))
    img_path = "Photos/carros_2.png"
    show.show_image(img_path,scale=1, object_detection=True, model=model,  min_confidence=50, detection_area=detection_area)

    detection_area= ((10,200),(400,600))
    img_path = "Photos/carros_2.png"
    show.show_image(img_path,scale=1, object_detection=True, model=model,  min_confidence=50, detection_area=detection_area)
    
    detection_area= ((50,50),(300,600))
    show.show_video(0, object_detection=True, model=model, frames=30, min_confidence=50,detection_area=detection_area)


if __name__ == "__main__":
    main()