import cv2 as cv
import numpy as np

def get_path(img_path):
    if isinstance(img_path, str):
        img = cv.imread(img_path)
        if img is None:
            print(f"Erro: Não foi possível carregar a imagem no caminho '{img_path}'.")
            return None, None, None
    else:
        img = img_path
    return img

def draw_blank_img(width=None,height=None, name=None, color=(0,0,0), get=True):
    """
    width -> the width of the blank image.
    height -> the height of the blank image.
    color -> RGB.
    """
    blank = np.zeros((height,width,3),dtype='uint8')
    blank[:]=color[2],color[1],color[0]
    if(get):
        return blank
    cv.imshow(name, blank)
    cv.waitKey(0)
    cv.destroyAllWindows()

def draw_rectangles(img_path=None, width=None, height=None, rects=None, name='Image', color=(0, 0, 0), get=True):
    """ 
    width -> Largura da imagem em branco.
    height -> Altura da imagem em branco.
    rects -> Lista de tuplas definindo cada retângulo. Cada tupla deve ser no formato ((x1, y1), (x2, y2), thickness).
    color -> Cor dos retângulos em formato RGB.
    name -> Nome da janela de exibição.
    """
    if(not rects):
       print("NO PARAMETERS")
       return

    if(img_path is not None):
        img = get_path(img_path)
    else:
        img = np.zeros((height, width, 3), dtype='uint8')

    # Desenhar cada retângulo da lista
    for rect in rects:
        top_left, bottom_right, thickness = rect
        cv.rectangle(img, top_left, bottom_right, (color[2], color[1], color[0]), thickness)

    if(get):
        return img
    
    # Exibir a imagem com os retângulos
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def draw_circles(img_path=None, width=None, height=None, circles=None, name='Image', color=(0, 0, 0), get=True):
    """
    width -> Largura da imagem em branco.
    height -> Altura da imagem em branco.
    circles -> Lista de tuplas definindo cada circulo. Cada tupla deve ser no formato ((x1, y1), radius, thickness).
    color -> Cor dos retângulos em formato RGB.
    name -> Nome da janela de exibição.
    """

    if(not circles):
       print("NO PARAMETERS")
       return
    
    if(img_path is not None):
        img = get_path(img_path)
    else:
        img = np.zeros((height, width, 3), dtype='uint8')

    for circle in circles:
        center, radius, thickness = circle
        cv.circle(img, center, radius, (color[2], color[1], color[0]), thickness)

    if(get):
        return img
    
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()    

def draw_lines(img_path=None, width=None, height=None, lines=None, name='Image', color=(0, 0, 0), get=True):
    """
    width -> Largura da imagem em branco.
    height -> Altura da imagem em branco.
    lines -> Lista de tuplas definindo cada linha. Cada tupla deve ser no formato ((x1, y1), (x2, y2), thickness).
    color -> Cor dos retângulos em formato RGB.
    name -> Nome da janela de exibição.
    """

    if(not lines):
       print("NO PARAMETERS")
       return

    if(img_path is not None):
        img = get_path(img_path)
    else:
        img = np.zeros((height, width, 3), dtype='uint8')

    # Desenhar cada retângulo da lista
    for line in lines:
        x1, x2, thickness = line
        cv.line(img, x1, x2, (color[2], color[1], color[0]), thickness)

    if(get):
        return img
    
    # Exibir a imagem com os retângulos
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()    

def draw_words(img_path=None, width=None, height=None, words=None, name='Image', color=(0, 0, 0), get=True):
    """
    width -> Largura da imagem em branco.
    height -> Altura da imagem em branco.
    lines -> Lista de tuplas definindo cada linha. Cada tupla deve ser no formato ((x1, y1), (x2, y2), thickness).
    color -> Cor dos retângulos em formato RGB.
    name -> Nome da janela de exibição.
    """
    if(not words):
       print("NO PARAMETERS")
       return
       
    if(img_path is not None):
        img = get_path(img_path)
    else:
        img = np.zeros((height, width, 3), dtype='uint8')

    # Desenhar cada retângulo da lista
    for word in words:
        text, position, font, scale, thickness = word
        cv.putText(img, text, position, font, scale, (color[2], color[1], color[0]), thickness)

    if(get):
        return img
    
    # Exibir a imagem com os retângulos
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()                