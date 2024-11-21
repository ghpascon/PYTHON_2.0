# run.py

from app.json_handler import read_json, update_json

def main():
    file_path = 'config.json'

    # Ler dados do JSON
    data = read_json(file_path)
    print("Dados lidos:", data)

    # Atualizar dados no JSON
    updates = {"age": 31}  # Exemplo: atualizar a idade para 31
    update_json(file_path, updates)
    print("Dados atualizados com sucesso!")

    # Ler dados atualizados
    updated_data = read_json(file_path)
    print("Dados atualizados:", updated_data)

if __name__ == '__main__':
    main()
