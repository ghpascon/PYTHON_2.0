import torch
from torchvision import models, transforms
from PIL import Image
import json
import torch.nn.functional as F  # Import softmax function
from functions.img_size import img_size

# Load the label mapping
def load_label_map(label_map_path='model/label_map.json'):
    """Load label mapping from a JSON file."""
    with open(label_map_path, 'r') as f:
        label_map = json.load(f)
    return label_map

def load_model(model_path='model/model.pth'):
    """Load the pre-trained model with weights."""
    model = models.resnet18(weights="IMAGENET1K_V1")
    model.fc = torch.nn.Linear(model.fc.in_features, len(load_label_map()))  # Adjust final layer

    # Load model weights and set the model to evaluation mode
    model.load_state_dict(torch.load(model_path, weights_only=True))  # Use weights_only=True
    model.eval()  # Set the model to evaluation mode
    return model

# Define the image transformation
transform = transforms.Compose([
    transforms.Resize(img_size),  # Resize images
    transforms.ToTensor(),  # Convert to tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize
])

def predict_image(model, label_map, image_path):
    """Predict the category of an image and return the label and confidence."""
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0)  # Add batch dimension
    output = model(image)  # Make prediction
    
    # Calculate probabilities with softmax
    probabilities = F.softmax(output, dim=1)  # Normalize the output to probabilities
    _, predicted = torch.max(output, 1)  # Get the index of the highest probability class
    
    # Get the probability of the predicted class
    confidence = probabilities[0][predicted].item() * 100  # Convert to percentage
    
    category_name = label_map[str(predicted.item())]  # Map the index to the category name
    return category_name, confidence
