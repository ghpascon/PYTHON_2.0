import cv2 as cv
import numpy as np
from functions import basics
import os

def haarcascade_detection(img_path=None, haar_cascade_path=None, scaleFactor=1.1, minNeighbors=3, min_distance=50):
    img = basics.get_img(img_path)
    haar_cascade = cv.CascadeClassifier(haar_cascade_path)
    faces_rect = haar_cascade.detectMultiScale(img, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    
    # Lista para armazenar as detecções filtradas
    filtered_faces = []

    # Verificar duplicatas baseadas na distância mínima entre centros
    for (x, y, w, h) in faces_rect:
        center = np.array([x + w // 2, y + h // 2])
        is_duplicate = False

        # Comparar com cada centro já adicionado
        for (fx, fy, fw, fh) in filtered_faces:
            fcenter = np.array([fx + fw // 2, fy + fh // 2])
            distance = np.linalg.norm(center - fcenter)
            if distance < min_distance:
                is_duplicate = True
                break
        
        # Se não for duplicado, adicionar à lista de faces filtradas
        if not is_duplicate:
            filtered_faces.append((x, y, w, h))

    return filtered_faces
  
def get_rect(faces_rects):
    return [((x, y), (x + w, y + h), 2) for (x, y, w, h) in faces_rects]

def video_haarcascade_detection(video=None, haar_cascade_path=None, scaleFactor=1.1, minNeighbors=3, min_distance=50, scale=0.5, detection_interval=5, name="Video"):
    """
    Realiza detecção de rostos em tempo real usando um classificador Haar em um vídeo ou feed de câmera, com otimizações para melhorar a performance.

    Parâmetros:
    - video: Caminho para o arquivo de vídeo ou índice do dispositivo de câmera.
    - haar_cascade_path: Caminho para o arquivo XML do classificador Haar.
    - scaleFactor: Fator de escala para a imagem durante a detecção de rosto.
    - minNeighbors: Número mínimo de vizinhos para a detecção.
    - min_distance: Distância mínima entre os centros dos rostos detectados para evitar duplicatas.
    - scale: Fator de escala para redimensionar o frame para detecção (default=0.5 para otimização).
    - detection_interval: Número de frames entre cada detecção de rosto (para otimização).
    - name: Nome da janela de exibição.

    Retorna:
    - Exibe o vídeo com retângulos ao redor dos rostos detectados em tempo real.
    """
    capture = cv.VideoCapture(video)
    haar_cascade = cv.CascadeClassifier(haar_cascade_path)

    frame_count = 0
    faces_rect = []

    while True:
        isTrue, frame = capture.read()

        # Verifique se o frame foi capturado com sucesso
        if not isTrue:
            print("Erro: Não foi possível capturar o frame do vídeo.")
            break

        # Redimensiona o frame para acelerar a detecção
        if scale != 1:
            small_frame = cv.resize(frame, (0, 0), fx=scale, fy=scale)
        else:
            small_frame = frame

        # Executa a detecção a cada 'detection_interval' frames
        if frame_count % detection_interval == 0:
            # Converte para escala de cinza para a detecção mais rápida
            gray_frame = cv.cvtColor(small_frame, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray_frame, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

            # Filtra duplicados com base na distância mínima
            filtered_faces = []
            for (x, y, w, h) in faces_rect:
                center = (x + w // 2, y + h // 2)
                is_duplicate = False
                for (fx, fy, fw, fh) in filtered_faces:
                    fcenter = (fx + fw // 2, fy + fh // 2)
                    distance = ((center[0] - fcenter[0]) ** 2 + (center[1] - fcenter[1]) ** 2) ** 0.5
                    if distance < min_distance * scale:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    filtered_faces.append((x, y, w, h))
            faces_rect = filtered_faces

        # Redimensiona as coordenadas dos rostos detectados para o frame original
        rect_img = frame.copy()
        for (x, y, w, h) in faces_rect:
            x, y, w, h = int(x / scale), int(y / scale), int(w / scale), int(h / scale)
            cv.rectangle(rect_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Exibe a imagem com retângulos ao redor dos rostos detectados
        if rect_img is not None and rect_img.shape[0] > 0 and rect_img.shape[1] > 0:
            cv.imshow(name, rect_img)
        else:
            print("Erro: Imagem de saída inválida para exibição.")
            break

        # Pressione 'd' para sair
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
        
        frame_count += 1

    # Libera a captura e fecha todas as janelas abertas
    capture.release()
    cv.destroyAllWindows()

def create_train(paths=[], haar_cascade_path=None, scaleFactor=1.1, minNeighbors=3, min_distance=50):
    """
    Cria um conjunto de treino extraindo as faces das imagens com a ajuda de um classificador Haar.
    Utiliza a função de detecção personalizada com filtragem de duplicatas.

    :param paths: Lista de diretórios com imagens para treinamento.
    :param haar_cascade_path: Caminho para o arquivo Haar Cascade.
    :param scaleFactor: Fator de escala para a detecção de rostos.
    :param minNeighbors: Número mínimo de vizinhos para a detecção.
    :param min_distance: Distância mínima entre os centros das faces detectadas para evitar duplicatas.
    :return: Listas de características (faces) e labels (identificações).
    """
    features = []
    labels = []
    
    # Verificar se o caminho do Haar Cascade é válido
    if not os.path.exists(haar_cascade_path):
        print("Erro: O caminho para o Haar Cascade não é válido.")
        return [], []

    # Para cada diretório de imagens
    for label, path in enumerate(paths):
        if not os.path.isdir(path):
            print(f"Aviso: O caminho '{path}' não é um diretório válido.")
            continue
        
        # Para cada imagem no diretório
        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            
            # Verificar se é uma imagem válida (extensões como .jpg, .jpeg, .png)
            if not img_name.lower().endswith(('jpg', 'jpeg', 'png')):
                continue

            img_array = cv.imread(img_path)
            if img_array is None:
                continue  # Pular imagens que não podem ser carregadas

            # Converter para escala de cinza
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Detectar faces na imagem usando a função customizada
            faces_rect = haarcascade_detection(img_path=img_path, 
                                               haar_cascade_path=haar_cascade_path, 
                                               scaleFactor=scaleFactor, 
                                               minNeighbors=minNeighbors, 
                                               min_distance=min_distance)

            # Para cada face detectada, extraímos a região de interesse (ROI) e a adicionamos à lista de features
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
    
    # Converter para arrays numpy
    features = np.array(features, dtype='object')
    labels = np.array(labels)

    # Criar o reconhecedor de faces
    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    # Treinar o reconhecedor com as características e rótulos
    face_recognizer.train(features, labels)

    # Criar diretório 'train_model' caso não exista
    train_model_dir = 'train_model'
    if not os.path.exists(train_model_dir):
        os.makedirs(train_model_dir)

    # Salvar o modelo treinado, as features e os labels no diretório 'train_model'
    face_recognizer.save(os.path.join(train_model_dir, 'face_trained.yml'))
    np.save(os.path.join(train_model_dir, 'features.npy'), features)
    np.save(os.path.join(train_model_dir, 'labels.npy'), labels)

    print(f"Treinamento concluído e arquivos salvos em '{train_model_dir}'.")

def recognizer(img_path=None, haar_cascade_path=None, model_path=None, obj=[], scaleFactor=1.1, minNeighbors=4, min_distance=50):
    """
    Função que tenta identificar quem é a pessoa em uma imagem utilizando o modelo LBPH treinado.

    Parâmetros:
    - img_path: Caminho da imagem que será utilizada para reconhecimento facial.
    - haar_cascade_path: Caminho para o arquivo Haar Cascade (opcional).
    - model_path: Caminho para o modelo LBPH treinado (opcional).
    - scaleFactor: Fator de escala para a detecção de rostos.
    - minNeighbors: Número de vizinhos para a detecção de rostos.
    - min_distance: Distância mínima para considerar rostos como duplicados.

    Retorna:
    - A imagem com a face detectada e o nome da pessoa identificado.
    """
    # Carregar o classificador Haar
    haar_cascade = cv.CascadeClassifier(haar_cascade_path)

    # Carregar o modelo LBPH treinado
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read(model_path)

    # Carregar a imagem de entrada
    img = basics.get_img(img_path=img_path)
    if img is None:
        print("Erro ao carregar a imagem!")
        return None

    # Converter para escala de cinza
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Detectar rostos na imagem
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=(30, 30))

    # Lista para armazenar as faces filtradas (não duplicadas)
    filtered_faces = []

    # Filtrar faces duplicadas
    for (x, y, w, h) in faces_rect:
        center = np.array([x + w // 2, y + h // 2])
        is_duplicate = False

        # Comparar com cada centro já adicionado
        for (fx, fy, fw, fh) in filtered_faces:
            fcenter = np.array([fx + fw // 2, fy + fh // 2])
            distance = np.linalg.norm(center - fcenter)
            if distance < min_distance:
                is_duplicate = True
                break

        # Se não for duplicado, adicionar à lista de faces filtradas
        if not is_duplicate:
            filtered_faces.append((x, y, w, h))

    # Para cada face filtrada, realizar o reconhecimento
    for (x, y, w, h) in filtered_faces:
        faces_roi = gray[y:y + h, x:x + w]

        # Fazer a previsão (identificação) da face
        label, confidence = face_recognizer.predict(faces_roi)

        # Verificar se a confiança é boa o suficiente para identificar a pessoa
        if confidence < 100:
            name = obj[label]
        else:
            name = "Desconhecido"

        print(f'Pessoa identificada: {name} com confiança de {confidence:.2f}')

        # Aqui, você pode desenhar o retângulo e o nome na imagem, se necessário
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv.putText(img, name, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Retornar a imagem com os rostos detectados e identificados
    return img