# app/json_handler.py

import json

def read_json(file_path):
    """Ler dados de um arquivo JSON."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON no arquivo {file_path}.")
        return {}

def update_json(file_path, updates):
    """Atualizar valores no arquivo JSON com base nas atualizações fornecidas."""
    data = read_json(file_path)
    
    # Atualizar os dados com os valores fornecidos
    data.update(updates)
    
    # Salvar os dados atualizados de volta ao arquivo
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
