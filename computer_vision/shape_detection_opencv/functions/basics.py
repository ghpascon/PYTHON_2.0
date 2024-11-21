import cv2 as cv
import numpy as np

def get_img(img_path):
    """
    Carrega a imagem a partir de um caminho ou retorna a imagem se já estiver carregada.
    """
    return cv.imread(img_path) if isinstance(img_path, str) else img_path

def normalized_img(img_path, level=1):
    """
    Normaliza a imagem com diferentes níveis de processamento:
    1 - Escala de cinza
    2 - Escala de cinza + Blur (desfoque)
    3 - Escala de cinza + Blur + Detecção de bordas
    4 - Escala de cinza + Blur + Bordas + Dilatação
    5 - Escala de cinza + Blur + Bordas + Dilatação + Erosão
    """
    img = get_img(img_path)    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    if level == 1:
        return gray

    blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
    if level == 2:
        return blur

    edge = cv.Canny(blur, 125, 175)
    if level == 3:
        return edge

    dilated = cv.dilate(edge, (3, 3), iterations=3)
    if level == 4:
        return dilated

    erode = cv.erode(dilated, (3, 3), iterations=1)
    return erode if level == 5 else gray

def scale_img(frame, scale):
    """
    Redimensiona a imagem com um fator de escala.
    """
    img = get_img(frame)
    new_size = (int(img.shape[1] * scale), int(img.shape[0] * scale))
    return cv.resize(img, new_size, interpolation=cv.INTER_AREA)

def resize_img(frame=None, dimensions=(0, 0)):
    """
    Redimensiona a imagem para as dimensões especificadas.
    """
    img = get_img(frame)
    if img is None:
        print(f"Erro: Imagem não encontrada.")
        return

    # Seleciona a interpolação ideal
    interpolation = cv.INTER_AREA if dimensions[0] < img.shape[1] else cv.INTER_CUBIC
    return cv.resize(img, dimensions, interpolation=interpolation)

def get_contour_img(img_path):
    """
    Encontra contornos na imagem e retorna uma imagem em branco com os contornos desenhados.
    """
    img = get_img(img_path)   
    contours, _ = cv.findContours(img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    print(f'{len(contours)} contornos encontrados.')

    blank = np.zeros((img.shape[0], img.shape[1], 3), dtype='uint8')
    cv.drawContours(blank, contours, -1, (255, 255, 255), 1)
    return blank

def thresholding(img_path=None, min_value=0, inverse=False):
    """
    Aplica limiarização à imagem.
    """
    img = get_img(img_path)
    code = cv.THRESH_BINARY_INV if inverse else cv.THRESH_BINARY

    if min_value == 0:
        return cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, code, 11, 9)

    _, thresh = cv.threshold(img, min_value, 255, code)
    return thresh

def edge_img(img_path=None, mode=0):
    """
    Aplica detecção de bordas na imagem.
    Modes:
    0 - Canny
    1 - Sobel X
    2 - Sobel Y
    3 - Sobel XY (X ou Y)
    4 - Laplaciano
    """
    img = get_img(img_path)
    
    if mode == 0:
        return cv.Canny(img, 150, 175)
    elif mode == 1:
        return cv.Sobel(img, cv.CV_64F, 1, 0)
    elif mode == 2:
        return cv.Sobel(img, cv.CV_64F, 0, 1)
    elif mode == 3:
        edge_x = cv.Sobel(img, cv.CV_64F, 1, 0)
        edge_y = cv.Sobel(img, cv.CV_64F, 0, 1)
        return cv.bitwise_or(edge_x, edge_y)
    elif mode == 4:
        laplacian = cv.Laplacian(img, cv.CV_64F)
        return np.uint8(np.absolute(laplacian))
