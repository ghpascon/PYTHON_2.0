from app.table_func import *

def main():
    file_path = find_xlsx_file()
    if file_path:
        result = extract_columns_from_xlsx(file_path)
        save_to_xlsx(result, 'resultado')
    else:
        print("Nenhum arquivo .xlsx encontrado na pasta.")

if __name__ == '__main__':
    main()

#pyinstaller --onefile --add-data "app;app" run.py
