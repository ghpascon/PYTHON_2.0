import cv2 as cv
from functions import basics
import math

def calculate_distance(center1, center2):
    """Calcula a distância euclidiana entre dois centros"""
    return math.sqrt((center1[0] - center2[0])**2 + (center1[1] - center2[1])**2)

def detect_objects(image, model, min_distance=50, confidence_threshold=60, detection_area=None):
    """
    Detecta objetos na imagem e aplica uma distância mínima entre centros para filtrar objetos próximos.
    
    image -> imagem a ser processada
    model -> modelo de detecção de objetos
    min_distance -> distância mínima entre centros de objetos para considerar como diferentes
    confidence_threshold -> confiança mínima para considerar uma detecção válida
    detection_area -> área de detecção como uma tupla ((x_min, y_min), (x_max, y_max))
    
    Retorna a lista de objetos detectados e um dicionário com a contagem de objetos por tipo.
    """
    # Realizar a detecção com o modelo
    results = model(image)
    
    # Obter as detecções como um DataFrame do Pandas
    detections = results.pandas().xyxy[0]  # Coordenadas e detalhes das detecções
    
    # Lista de objetos detectados
    objects = []
    detected_centers = []  # Lista para armazenar os centros dos objetos já detectados
    count_by_type = {}  # Dicionário para armazenar a contagem de objetos por tipo

    # Verificar se uma área de detecção foi definida
    if detection_area is not None:
        # Descompactar a área de detecção para obter as coordenadas
        (x_min_area, y_min_area), (x_max_area, y_max_area) = detection_area
    else:
        # Se a área de detecção não for fornecida, definir como a área total da imagem
        x_min_area, y_min_area, x_max_area, y_max_area = 0, 0, image.shape[1], image.shape[0]

    for _, row in detections.iterrows():
        x_min, y_min, x_max, y_max = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        object_type = row['name']  # Nome do tipo de objeto (sem a confiança)
        confidence = row['confidence'] * 100  # Porcentagem de confiança

        # Ignorar detecções com confiança abaixo do limite definido
        if confidence < confidence_threshold:
            continue
        
        # Calcular o centro da caixa delimitadora
        center = ((x_min + x_max) // 2, (y_min + y_max) // 2)
        
        # Verificar se o centro do objeto está dentro da área de detecção
        if not (x_min_area <= center[0] <= x_max_area and y_min_area <= center[1] <= y_max_area):
            continue  # Ignorar objetos fora da área de detecção

        # Verificar se o objeto está suficientemente distante dos objetos já detectados
        is_close = False
        for prev_center in detected_centers:
            if calculate_distance(center, prev_center) < min_distance:
                is_close = True
                break
        
        # Se o objeto não estiver muito próximo de outro, adicionar à lista
        if not is_close:
            objects.append({
                'label': object_type,
                'confidence': confidence,
                'coordinates': (x_min, y_min, x_max, y_max)
            })
            detected_centers.append(center)  # Adicionar o centro do objeto à lista
            
            # Mostrar o tipo do objeto e sua confiança
            print(f"{object_type} - {confidence:.2f}% confidence")

        # Contar os objetos por tipo (sem a confiança)
        if object_type not in count_by_type:
            count_by_type[object_type] = 0
        count_by_type[object_type] += 1

    # Exibir a contagem de objetos por tipo
    for obj_type, count in count_by_type.items():
        print(f"{obj_type}: {count} found")

    return objects  # Retorna os objetos detectados e a contagem por tipo
