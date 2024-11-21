from app.app import upload_program_to_esp, generate_littlefs_bin, get_config_path
 
def main():
    input_folder = "data"
    output_folder = "bin_files"
    generate_littlefs_bin(input_folder, output_folder)

    upload_program_to_esp()

if __name__ == "__main__":
    main()
    input("...")

#pyinstaller --onefile --add-data "app;app" --add-data "esp_depend;esp_depend" run.py
