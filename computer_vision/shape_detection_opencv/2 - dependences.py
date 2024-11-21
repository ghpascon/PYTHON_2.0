import subprocess
import os

def install_dependencies():
    # Executar o comando para instalar as dependências
    subprocess.run(["pip", "install", "-r", "yolov5/requirements.txt"])
    print("Dependências instaladas com sucesso.")

install_dependencies()
