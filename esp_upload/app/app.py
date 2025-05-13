import subprocess
import json
import os
import sys
import glob


def upload_program_to_esp():
    config = load_config("config/config.json")
    port = config["com_port"]
    esp32s3 = config["esp32s3"]

    # Solicitar caminhos relativos
    bootloader_path = glob.glob(os.path.join("bin_files", '*.ino.bootloader.bin'))[0]
    partitions_path = glob.glob(os.path.join("bin_files", '*.ino.partitions.bin'))[0]
    app_path = glob.glob(os.path.join("bin_files", '*.ino.bin'))[0]
    bin_data="bin_files/littlefs.bin"

    # Definir o caminho absoluto para o boot_app0.bin (se necessário)
    esptool_path=get_config_path("esp_depend/esptool.exe")
    boot_app0_path = get_config_path("esp_depend/boot_app0.bin")


    # Definir outros parâmetros
    baud_rate = "921600"
    flash_mode = "dio"
    flash_freq = "80m"
    flash_size = "4MB"
    boot_location = "0x0" if esp32s3 else "0x1000"

    # Gerar o comando
    command = (
        f' "{esptool_path}" '
        f'--chip auto  --port "{port}" --baud {baud_rate} '
        f'--before default_reset --after hard_reset write_flash -z '
        f'--flash_mode {flash_mode} --flash_freq {flash_freq} --flash_size {flash_size} '
        f'{boot_location} "{bootloader_path}" 0x8000 "{partitions_path}" 0xe000 "{boot_app0_path}" 0x10000 "{app_path}" 0x290000 "{bin_data}"'
    )

    # Exibir o comando para verificação
    print("Comando a ser executado:")
    print(command)

    # Executar o comando
    try:
        subprocess.run(command, shell=True, check=True)
        print("Comando executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")

def generate_littlefs_bin(input_folder, output_folder):
    # Caminho para o executável mklittlefs
    mklittlefs_exe = get_config_path("esp_depend/mklittlefs.exe")

    # Parâmetros específicos do comando
    page_size = 256
    block_size = 4096
    total_size = 1441792

    # Caminho completo para o arquivo de saída
    output_bin = os.path.join(output_folder, "littlefs.bin")

    # Construindo o comando
    command = [
        mklittlefs_exe,
        "-c", os.path.abspath(input_folder),
        "-p", str(page_size),
        "-b", str(block_size),
        "-s", str(total_size),
        os.path.abspath(output_bin)
    ]

    # Executando o comando
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Comando executado com sucesso!")
        print("Saída:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando:", e)
        print("Saída de erro:", e.stderr)

def get_config_path(filename):
    if getattr(sys, 'frozen', False):
        # Se estiver executando a partir de um executável PyInstaller
        partes = filename.split('/')
        print(partes)
        if len(partes) > 1:
            return os.path.join(sys._MEIPASS,partes[0],partes[1])
        else:
            return os.path.join(sys._MEIPASS,filename)
    else:
        # Se estiver executando a partir do código-fonte
        return filename
   
def load_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)
