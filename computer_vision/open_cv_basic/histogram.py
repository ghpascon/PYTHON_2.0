import cv2 as cv
from functions import show, draw, bitwise, color_img
import matplotlib.pyplot as plt

def main():
    img = "Photos/cats.jpg"

    # Obtendo o histograma de cores da imagem
    color_hist = color_img.histogram(img_path=img)
    plt.figure()
    plt.title(f"Color Histogram of {img}")
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
    plt.plot(color_hist['b'], color='b')  # Canal azul
    plt.plot(color_hist['g'], color='g')  # Canal verde
    plt.plot(color_hist['r'], color='r')  # Canal vermelho
    plt.xlim(0, 256)
    plt.show()

    # Obtendo o histograma em escala de cinza da imagem
    gray_hist = color_img.gray_histogram(img_path=img)
    plt.figure()
    plt.title(f"Grayscale Histogram of {img}")
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
    plt.plot(gray_hist, color='k')  # 'k' representa preto para o histograma em cinza
    plt.xlim(0, 256)
    plt.show()

if __name__ == "__main__":
    main()
