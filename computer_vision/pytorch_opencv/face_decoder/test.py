from functions.test import load_model, load_label_map, predict_image

def main():
    # Load the model and label_map
    model = load_model()
    label_map = load_label_map()

    for i in range(1, 6):
        image_path = f'test_img/ben_afflek/{i}.jpg' 
        category, confidence = predict_image(model, label_map, image_path)
        print(f'Image: {image_path}')
        print(f'The image is predicted as: {category}')
        print(f'Confidence: {confidence:.2f}%\n')

    for i in range(1, 6):
        image_path = f'test_img/elton_john/{i}.jpg' 
        category, confidence = predict_image(model, label_map, image_path)
        print(f'Image: {image_path}')
        print(f'The image is predicted as: {category}')
        print(f'Confidence: {confidence:.2f}%\n')

    for i in range(1, 6):
        image_path = f'test_img/jerry_seinfeld/{i}.jpg' 
        category, confidence = predict_image(model, label_map, image_path)
        print(f'Image: {image_path}')
        print(f'The image is predicted as: {category}')
        print(f'Confidence: {confidence:.2f}%\n')

    for i in range(1, 6):
        image_path = f'test_img/madonna/{i}.jpg' 
        category, confidence = predict_image(model, label_map, image_path)
        print(f'Image: {image_path}')
        print(f'The image is predicted as: {category}')
        print(f'Confidence: {confidence:.2f}%\n')

    for i in range(1, 6):
        image_path = f'test_img/mindy_kaling/{i}.jpg' 
        category, confidence = predict_image(model, label_map, image_path)
        print(f'Image: {image_path}')
        print(f'The image is predicted as: {category}')
        print(f'Confidence: {confidence:.2f}%\n')

if __name__ == "__main__":
    main()
