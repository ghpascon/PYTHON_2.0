import cv2
import numpy as np
import os

def detect_and_create_annotations(image_path, output_dir, class_index=0):
    # Carregar a imagem
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecção de círculos com a Transformada de Hough
    circles = cv2.HoughCircles(
        gray, 
        cv2.HOUGH_GRADIENT, dp=1.2, minDist=50, 
        param1=50, param2=30, minRadius=20, maxRadius=50
    )
    
    # Detecção de quadrados usando contornos
    squares = detect_squares(img)
    
    annotations_created = False
    
    # Verificar se círculos foram encontrados
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        # Criar o arquivo de anotação para círculos
        annotation_file = os.path.join(output_dir, os.path.basename(image_path).replace('.png', '.txt'))

        with open(annotation_file, 'w') as file:
            for (x, y, r) in circles:
                # Normalizar as coordenadas para o formato YOLO
                height, width, _ = img.shape
                x_center = x / width
                y_center = y / height
                circle_width = r * 2 / width  # largura da caixa (2 vezes o raio)
                circle_height = r * 2 / height  # altura da caixa (2 vezes o raio)

                # Salvar as anotações no formato YOLO (classe, x_center, y_center, width, height)
                file.write(f"{class_index} {x_center} {y_center} {circle_width} {circle_height}\n")

                # Desenhar o círculo na imagem
                cv2.circle(img, (x, y), r, (0, 255, 0), 4)

        annotations_created = True
        print(f"Anotações para círculos em {image_path} salvas em {annotation_file}")
    
    # Verificar se quadrados foram encontrados
    if squares:
        # Criar o arquivo de anotação para quadrados
        annotation_file = os.path.join(output_dir, os.path.basename(image_path).replace('.png', '.txt'))

        with open(annotation_file, 'a') as file:
            for (x, y, w, h) in squares:
                # Normalizar as coordenadas para o formato YOLO
                height, width, _ = img.shape
                x_center = (x + w / 2) / width
                y_center = (y + h / 2) / height
                box_width = w / width
                box_height = h / height

                # Salvar as anotações no formato YOLO (classe, x_center, y_center, width, height)
                file.write(f"1 {x_center} {y_center} {box_width} {box_height}\n")

                # Desenhar o quadrado na imagem
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)
        
        annotations_created = True
        print(f"Anotações para quadrados em {image_path} salvas em {annotation_file}")
    
    # Se nenhuma anotação for criada, retornar False
    if not annotations_created:
        print(f"Nenhum círculo ou quadrado encontrado na imagem {image_path}")

    # Mostrar a imagem com os círculos e quadrados desenhados
    cv2.imshow("Image with Annotations", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_squares(img):
    """
    Detecta quadrados na imagem.
    Retorna uma lista de quadrados encontrados como (x, y, largura, altura).
    """
    squares = []
    # Converter para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplicar o Canny para detecção de bordas
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # Encontrar os contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Aproximar o contorno
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Se o contorno tiver 4 lados e for um quadrado (ângulos próximos de 90 graus)
        if len(approx) == 4 and cv2.isContourConvex(approx):
            (x, y, w, h) = cv2.boundingRect(approx)
            aspect_ratio = w / h
            
            # Considera-se quadrado se a razão de aspecto for aproximadamente 1
            if 0.8 < aspect_ratio < 1.2:
                squares.append((x, y, w, h))
    
    return squares

def process_images(input_dir, output_dir):
    # Inicializar contadores de círculos e quadrados
    circle_count = 0
    square_count = 0

    # Criar a pasta de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    # Listar todas as imagens na pasta de entrada
    for filename in os.listdir(input_dir):
        image_path = os.path.join(input_dir, filename)
        
        # Verificar se o arquivo é uma imagem e se começa com 'c_' ou 'q_'
        if filename.endswith('.png'):
            if filename.startswith('c_'):
                # Gerar anotações para círculos
                detect_and_create_annotations(image_path, output_dir, class_index=0)
                circle_count += 1
            elif filename.startswith('q_'):
                # Gerar anotações para quadrados
                detect_and_create_annotations(image_path, output_dir, class_index=1)
                square_count += 1

    # Exibir contagem de círculos e quadrados
    print(f"Total de imagens de círculos (c_): {circle_count}")
    print(f"Total de imagens de quadrados (q_): {square_count}")

# Caminhos de entrada e saída
input_dir = "model/images/train"  # Caminho da pasta com as imagens
output_dir = "model/annotations"  # Caminho da pasta de anotações

# Processar as imagens e gerar as anotações
process_images(input_dir, output_dir)
