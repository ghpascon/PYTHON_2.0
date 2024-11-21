import cv2
import numpy as np
import os

def detectar_circulos(imagem_path):
    # Carregar a imagem
    imagem = cv2.imread(imagem_path, cv2.IMREAD_COLOR)

    # Verificar se a imagem foi carregada corretamente
    if imagem is None:
        print("Erro ao carregar a imagem.")
        return
    else:
        # Converter para escala de cinza
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        
        # Aplicar um desfoque para reduzir o ruído
        imagem_cinza = cv2.medianBlur(imagem_cinza, 5)
        
        # Detectar círculos usando HoughCircles
        circulos = cv2.HoughCircles(
            imagem_cinza, 
            cv2.HOUGH_GRADIENT, 
            dp=1.2,         # Resolução da detecção
            minDist=150,     # Aumentar a distância mínima entre centros
            param1=50,      # Parâmetro do detector de bordas Canny
            param2=50,      # Aumentar para reduzir a sensibilidade
            minRadius=25,   # Raio mínimo do círculo
            maxRadius=50   # Raio máximo do círculo
        )
        
        # Verificar se algum círculo foi encontrado
        if circulos is not None:
            # Arredondar e converter para inteiros
            circulos = np.uint16(np.around(circulos))
            
            # Mostrar a quantidade de círculos detectados
            print(f"Número de círculos detectados: {len(circulos[0])}")
            
            # Desenhar os círculos encontrados
            for i in circulos[0, :]:
                # Desenhar o círculo externo
                cv2.circle(imagem, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # Desenhar o centro do círculo
                cv2.circle(imagem, (i[0], i[1]), 2, (0, 0, 255), 3)
            
            # Mostrar a imagem com os círculos
            cv2.imshow("Círculos Detectados", imagem)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Nenhum círculo foi encontrado.")

if __name__ == "__main__":
    imagem_path = "img/img_5.webp"    
    detectar_circulos(imagem_path)
