import torch
from pathlib import Path
from PIL import Image
import requests
from io import BytesIO

def test_yolov5_model():
    # Carregar o modelo pré-treinado (yolov5s é um modelo pequeno e rápido)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # ou 'yolov5m', 'yolov5l', 'yolov5x' para modelos maiores

    # Baixar uma imagem de teste
    url = "https://ultralytics.com/images/zidane.jpg"  # Link de imagem de teste
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Realizar a detecção
    results = model(img)
    
    # Exibir resultados
    results.show()  # Mostrar a imagem com as detecções
    results.print()  # Imprimir informações de detecção no console

test_yolov5_model()
