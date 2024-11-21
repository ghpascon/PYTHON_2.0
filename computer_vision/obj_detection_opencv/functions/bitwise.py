import cv2 as cv

def bitwise_and(img_1, img_2):
    """
    Retorna a interseção (AND) entre duas imagens.
    Ambas as imagens devem ter as mesmas dimensões e tipo.
    
    Parameters:
    - img_1: Primeira imagem para a operação AND.
    - img_2: Segunda imagem para a operação AND.
    
    Returns:
    - Imagem resultante da operação bitwise AND entre img_1 e img_2.
    """
    return cv.bitwise_and(img_1, img_2)

def bitwise_or(img_1, img_2):
    """
    Retorna a união (OR) entre duas imagens.
    Ambas as imagens devem ter as mesmas dimensões e tipo.
    
    Parameters:
    - img_1: Primeira imagem para a operação OR.
    - img_2: Segunda imagem para a operação OR.
    
    Returns:
    - Imagem resultante da operação bitwise OR entre img_1 e img_2.
    """
    return cv.bitwise_or(img_1, img_2)

def bitwise_xor(img_1, img_2):
    """
    Retorna a diferença simétrica (XOR) entre duas imagens.
    Ambas as imagens devem ter as mesmas dimensões e tipo.
    
    Parameters:
    - img_1: Primeira imagem para a operação XOR.
    - img_2: Segunda imagem para a operação XOR.
    
    Returns:
    - Imagem resultante da operação bitwise XOR entre img_1 e img_2.
    """
    return cv.bitwise_xor(img_1, img_2)

def bitwise_not(img_1):
    """
    Inverte os bits da imagem (NOT), transformando cada pixel em seu complemento.
    
    Parameters:
    - img_1: Imagem para a qual a operação NOT será aplicada.
    
    Returns:
    - Imagem resultante da operação bitwise NOT de img_1.
    """
    return cv.bitwise_not(img_1)
