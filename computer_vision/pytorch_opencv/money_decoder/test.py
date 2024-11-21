from functions.test import load_model, load_label_map, predict_image

def main():
    # Load the model and label_map
    model = load_model()
    label_map = load_label_map()

    image_path = 'teste_img/image.png' 
    category, confidence = predict_image(model, label_map, image_path)
    print(f'Image: {image_path}')
    print(f'The image is predicted as: {category}')
    print(f'Confidence: {confidence:.2f}%\n')

if __name__ == "__main__":
    main()
