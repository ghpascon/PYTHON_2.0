# run.py

from app.json_handler import read_json, update_json

def main():
    config = read_json()
    print("Configuração carregada:", config)

    if config:
        updates = {"name":"Gabriel","age": 31}  
        update_json(updates)

        updated_config = read_json()
        print("Configuração atualizada:", updated_config)

if __name__ == '__main__':
    main()
