from app import app

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8000, debug=False)

#pip install pyinstaller
#pyinstaller --onefile --windowed --add-data "app;app" --add-data "mysql_python;mysql_python" --add-data "config;config" run.py
#pyinstaller --onefile --add-data "app;app" --add-data "mysql_python;mysql_python" --add-data "config;config" run.py
