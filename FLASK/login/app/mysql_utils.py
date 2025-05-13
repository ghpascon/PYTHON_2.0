import mysql.connector

# Função para conectar ao banco
def get_db_connection(db_config):
    return mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )