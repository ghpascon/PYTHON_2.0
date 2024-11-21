import cv2 as cv
import numpy as np
from functions import basics

def load_image(img_path):
    """
    Função auxiliar para carregar a imagem de um caminho ou retornar a imagem fornecida.
    img_path -> Caminho para a imagem ou a imagem já carregada.
    Retorna a imagem carregada.
    """
    if isinstance(img_path, str):
        img = cv.imread(img_path)
        if img is None:
            print(f"Erro: Não foi possível carregar a imagem no caminho '{img_path}'.")
            return None
    else:
        img = img_path
    return img

def merge_colors(b_channel, g_channel, r_channel):
    """
    Combina os canais de cor B, G e R em uma única imagem.
    b_channel -> Canal azul.
    g_channel -> Canal verde.
    r_channel -> Canal vermelho.
    Retorna a imagem combinada ou None em caso de erro.
    """
    # Verificar se os canais têm a mesma dimensão
    if b_channel.shape != g_channel.shape or b_channel.shape != r_channel.shape:
        print("Erro: Todos os canais devem ter a mesma dimensão.")
        return None

    # Combinar os canais em uma única imagem BGR
    merged_image = cv.merge([b_channel, g_channel, r_channel])
    return merged_image

def split_colors(img_path):
    """
    Divide a imagem em suas componentes de cor: azul, verde e vermelho.
    img_path -> Caminho para a imagem ou a imagem carregada.
    Retorna três imagens: (B, G, R).
    """
    img = load_image(img_path)
    if img is None:
        return None, None, None

    # Dividir a imagem em suas componentes de cor
    b, g, r = cv.split(img)
    return b, g, r

def color_converter(img_path, code):
    """
    Converte a imagem para o código de cor especificado.
    img_path -> Caminho para a imagem ou a imagem carregada.
    code -> Código de conversão de cor (ex: cv.COLOR_BGR2GRAY).
    Retorna a imagem convertida.
    """
    img = load_image(img_path)
    if img is None:
        return None

    color_img = cv.cvtColor(img, code)
    return color_img

def grayscale_img(img_path):
    """
    Converte a imagem para escala de cinza.
    img_path -> Caminho para a imagem ou a imagem carregada.
    Retorna a imagem em escala de cinza.
    """
    return color_converter(img_path, cv.COLOR_BGR2GRAY)

def hsv_img(img_path):
    """
    Converte a imagem para o espaço de cores HSV.
    img_path -> Caminho para a imagem ou a imagem carregada.
    Retorna a imagem no espaço HSV.
    """
    return color_converter(img_path, cv.COLOR_BGR2HSV)

def lab_img(img_path):
    """
    Converte a imagem para o espaço de cores LAB.
    img_path -> Caminho para a imagem ou a imagem carregada.
    Retorna a imagem no espaço LAB.
    """
    return color_converter(img_path, cv.COLOR_BGR2LAB)

def rgb_img(img_path):
    """
    Converte a imagem para o espaço de cores RGB.
    img_path -> Caminho para a imagem ou a imagem carregada.
    Retorna a imagem no espaço RGB.
    """
    return color_converter(img_path, cv.COLOR_BGR2RGB)

def histogram(img_path=None):
    """
    Calcula o histograma de uma imagem.
    img_path -> Caminho para a imagem ou a imagem carregada.
    Retorna um dicionário com os histogramas dos canais 'b', 'g', 'r'.
    """
    img = load_image(img_path)
    if img is None:
        return None

    colors = ('b', 'g', 'r')
    hist = {}
    for i, col in enumerate(colors):
        hist[col] = cv.calcHist([img], [i], None, [256], [0, 256])
    return hist

def gray_histogram(img_path=None, channel=0):
    """
    Calcula o histograma de uma imagem em escala de cinza (ou canal específico).
    img_path -> Caminho para a imagem ou a imagem carregada.
    channel -> Canal específico a ser analisado, geralmente 0 para uma imagem em escala de cinza.
    Retorna o histograma.
    """
    img = load_image(img_path)
    if img is None:
        return None

    normalized_img = basics.normalized_img(img, 1)  # Normalização de imagem se necessário
    gray_hist = cv.calcHist([normalized_img], [channel], None, [256], [0, 256])
    return gray_hist
