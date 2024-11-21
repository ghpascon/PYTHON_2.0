import mysql.connector
import json
import sys
import os

def get_config_path():
    if getattr(sys, 'frozen', False):
        # Se estiver executando a partir de um executável PyInstaller
        return os.path.join(sys._MEIPASS, 'config', 'config.json')
    else:
        # Se estiver executando a partir do código-fonte
        return 'config/config.json'

def get_db_config():
    config_path = get_config_path()
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config

def get_db_connection():
    config = get_db_config()
    connection = mysql.connector.connect(
        host=config['host_address'],
        user=config['my_user'],
        password=config['my_password'],
        database=config['my_database']
    )
    return connection

def insert_user(name, email):
    try:
        config = get_db_config()
        connection = get_db_connection()
        cursor = connection.cursor()
        query = f"INSERT INTO {config['table_name']} (name, email) VALUES (%s, %s)"
        values = (name, email)
        cursor.execute(query, values)
        
        connection.commit()
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        print("Error connecting to the database:", error)    

def read_table():
    try:
        config = get_db_config()
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)  # Use dictionary=True to get results as dictionaries
        query = f"SELECT * FROM {config['table_name']}"
        cursor.execute(query)
        
        results = cursor.fetchall()  # Fetch all rows from the executed query
        cursor.close()
        connection.close()
        
        return results
    except mysql.connector.Error as error:
        print("Error reading the table:", error)
        return []
    
def clear_table():
    try:
        config = get_db_config()
        connection = get_db_connection()
        cursor = connection.cursor()
        query = f"TRUNCATE TABLE {config['table_name']}"
        cursor.execute(query)
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Table cleared successfully.")
    except mysql.connector.Error as error:
        print("Error clearing the table:", error)
