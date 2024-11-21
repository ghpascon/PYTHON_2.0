import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import models, transforms
from PIL import Image
from sklearn.model_selection import train_test_split
import json
from torch.utils.data import Dataset

def load_data(train_dir, max_data=None):
    # Obter todos os subdiretórios (categorias)
    subfolders = [f.path for f in os.scandir(train_dir) if f.is_dir()]
    label_map = {}
    image_paths = []
    labels = []
    total_images = 0
    
    # Iterar sobre cada subdiretório (categoria)
    for label, folder in enumerate(subfolders):
        names = os.path.basename(folder)
        label_map[label] = names
        
        # Obter todas as imagens (png, jpg, jpeg) dentro do subdiretório
        images = [f for f in os.listdir(folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

        if max_data is not None:
            images = images[:max_data]
        
        num_images = len(images)
        total_images += num_images
        
        # Exibir a quantidade de imagens por categoria
        print(f"Categoria: {names} - Imagens: {num_images}")
        
        for image in images:
            image_paths.append(os.path.join(folder, image))
            labels.append(label)
    
    # Exibir a quantidade total de imagens
    print(f"\nTotal de imagens: {total_images}")
    
    return image_paths, labels, label_map, total_images



# Definir transformações para as imagens com Data Augmentation
def get_transform():
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(20),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])


# Custom Dataset para carregar as imagens
class ArtistDataset(Dataset):
    def __init__(self, image_paths, labels, transform=None):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        image = Image.open(img_path).convert('RGB')
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label


# Função para dividir o dataset em treino e validação
def split_data(image_paths, labels):
    dataset = ArtistDataset(image_paths, labels, get_transform())
    train_dataset, val_dataset = train_test_split(list(zip(image_paths, labels)), test_size=0.2, stratify=labels)

    train_dataset = ArtistDataset([item[0] for item in train_dataset], [item[1] for item in train_dataset], get_transform())
    val_dataset = ArtistDataset([item[0] for item in val_dataset], [item[1] for item in val_dataset], get_transform())

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
    
    return train_loader, val_loader


# Função para definir o modelo
def define_model(label_map):
    model = models.resnet18(weights="IMAGENET1K_V1")
    model.fc = nn.Linear(model.fc.in_features, len(label_map))
    model.layer4[1].register_forward_hook(lambda self, input, output: torch.nn.functional.dropout(output, p=0.5, training=self.training))
    return model


# Função de treino com Early Stopping
def train_model(model, train_loader, val_loader, criterion, optimizer, scheduler, epochs=10, patience=5):
    best_val_loss = float('inf')
    epochs_without_improvement = 0

    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

        # Validar a precisão após cada época
        model.eval()
        val_loss = 0.0
        val_correct = 0
        val_total = 0
        with torch.no_grad():
            for inputs, labels in val_loader:
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                val_loss += loss.item()
                _, predicted = torch.max(outputs, 1)
                val_correct += (predicted == labels).sum().item()
                val_total += labels.size(0)

        val_accuracy = 100 * val_correct / val_total
        scheduler.step(val_loss)

        print(f"Epoch {epoch+1}/{epochs} - Loss: {running_loss/len(train_loader):.4f} - Accuracy: {100 * correct / total:.2f}%")
        print(f"Validation Loss: {val_loss/len(val_loader):.4f} - Validation Accuracy: {val_accuracy:.2f}%")

        # Early stopping
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            epochs_without_improvement = 0
            torch.save(model.state_dict(), 'best_model.pth')
        else:
            epochs_without_improvement += 1
            if epochs_without_improvement >= patience:
                print(f"Early stopping after {epoch+1} epochs.")
                break


# Função para salvar o modelo e o label_map
def save_model(model, label_map, model_path='model/model.pth', label_map_path='model/label_map.json'):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    torch.save(model.state_dict(), model_path)
    with open(label_map_path, 'w') as f:
        json.dump(label_map, f)
    print(f"Modelo e label_map salvos em {model_path} e {label_map_path}")
