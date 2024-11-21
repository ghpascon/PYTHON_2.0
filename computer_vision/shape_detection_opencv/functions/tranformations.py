import cv2 as cv
import numpy as np


def translate_img(img_path, x, y):
    """
    img_path -> Caminho para a imagem ou imagem já carregada.
    x -> Translação em pixels no eixo x.
    y -> Translação em pixels no eixo y.
    """
    # Verificar se o parâmetro `img_path` é um caminho ou uma imagem carregada
    if isinstance(img_path, str):
        img = cv.imread(img_path)
        if img is None:
            print(f"Erro: Não foi possível carregar a imagem no caminho '{img_path}'.")
            return None
    else:
        img = img_path

    # Definir a matriz de translação
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    # Retornar a imagem traduzida
    return cv.warpAffine(img, trans_mat, dimensions)

def rotate_img(img_path, angle, point=None):
    """
    img_path -> Caminho para a imagem ou imagem já carregada.
    angle -> Ângulo em graus para rotação.
    point -> Ponto de rotação (padrão: centro da imagem).
    """
    # Verificar se o parâmetro `img_path` é um caminho ou uma imagem carregada
    if isinstance(img_path, str):
        img = cv.imread(img_path)
        if img is None:
            print(f"Erro: Não foi possível carregar a imagem no caminho '{img_path}'.")
            return None
    else:
        img = img_path

    # Obter as dimensões da imagem
    height, width = img.shape[:2]
    if point is None:
        point = (width // 2, height // 2)

    # Definir a matriz de rotação
    rot_mat = cv.getRotationMatrix2D(point, angle, 1)
    dimensions = (width, height)

    # Retornar a imagem rotacionada
    return cv.warpAffine(img, rot_mat, dimensions)

def flip_img(frame=None, flip_code=0):
    """
    Espelha a imagem com base no flip_code especificado.
    
    frame -> Caminho para a imagem ou a imagem carregada.
    flip_code -> Valor indicando o tipo de espelhamento:
                 0 = Flip vertical
                 1 = Flip horizontal
                -1 = Flip vertical e horizontal
    """
    # Verificar se o parâmetro `frame` é um caminho de imagem (str) ou uma imagem carregada
    if isinstance(frame, str):
        img = cv.imread(frame)
        if img is None:
            print(f"Erro: Não foi possível carregar a imagem no caminho '{frame}'.")
            return
    else:
        img = frame

    # Realizar o espelhamento com base no flip_code
    flipped_img = cv.flip(img, flip_code)

    return flipped_img

def crop_img(frame=None, x=0, y=0, width=100, height=100):
    """
    Recorta uma imagem com base nas coordenadas e dimensões especificadas.
    
    frame -> Caminho para a imagem ou a imagem carregada.
    x -> Coordenada x do ponto de início do recorte.
    y -> Coordenada y do ponto de início do recorte.
    width -> Largura desejada para o recorte.
    height -> Altura desejada para o recorte.
    """
    # Verificar se o parâmetro `frame` é um caminho de imagem (str) ou uma imagem carregada
    if isinstance(frame, str):
        img = cv.imread(frame)
        if img is None:
            print(f"Erro: Não foi possível carregar a imagem no caminho '{frame}'.")
            return
    else:
        img = frame

    # Verificar se as coordenadas e dimensões de recorte são válidas
    if (x + width > img.shape[1]) or (y + height > img.shape[0]):
        print("Erro: As dimensões de recorte excedem o tamanho da imagem.")
        return

    # Realizar o recorte da imagem
    cropped_img = img[y:y + height, x:x + width]

    return cropped_img
