# app/json_handler.py

import json
import os
import sys

def get_config_path():
    """Obter o caminho do arquivo de configuração dependendo do ambiente de execução."""
    if getattr(sys, 'frozen', False):
        # Se estiver executando a partir de um executável PyInstaller
        return os.path.join(sys._MEIPASS, 'config', 'config.json')
    else:
        # Se estiver executando a partir do código-fonte
        return 'config/config.json'

def read_json():
    """Ler dados de um arquivo JSON."""
    file_path = get_config_path()
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON no arquivo {file_path}. Verifique o formato do arquivo.")
        return {}
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo {file_path}: {e}")
        return {}
    
def update_json(updates):
    """Atualizar valores no arquivo JSON com base nas atualizações fornecidas."""
    file_path = get_config_path()
    data = read_json()  # Usar read_json para obter os dados atuais
    
    # Atualizar os dados com os valores fornecidos
    data.update(updates)
    
    # Salvar os dados atualizados de volta ao arquivo
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Arquivo {file_path} atualizado com sucesso!")
    except IOError as e:
        print(f"Erro ao salvar o arquivo {file_path}: {e}")
