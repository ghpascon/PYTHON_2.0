import os
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from torch import nn
from functions.train import load_data, split_data, define_model, train_model, save_model, get_transform
from sklearn.model_selection import train_test_split

def main():
    train_dir = 'train_img'
    epochs=10

    # Carregar as imagens e rótulos
    image_paths, labels, label_map, total_images = load_data(train_dir)

    # Dividir o dataset em treino e validação
    train_loader, val_loader = split_data(image_paths, labels)

    # Definir o modelo
    print("definindo modelo")
    model = define_model(label_map)

    # Definir a função de perda e o otimizador
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.0001)

    # Definir o scheduler para ajustar o learning rate
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', patience=3, verbose=True)

    # Treinar o modelo
    print("treinando modelo")
    train_model(model, train_loader, val_loader, criterion, optimizer, scheduler, epochs=epochs, patience=3)

    # Salvar o modelo e o mapeamento de rótulos
    print("salvando modelo")
    save_model(model, label_map, model_path='model/model.pth', label_map_path='model/label_map.json')

if __name__ == "__main__":
    main()
