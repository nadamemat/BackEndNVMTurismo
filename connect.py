import mysql.connector

def get_db_connection():
    config = {
        'user': 'user1',
        'password': 'root',
        'host': 'localhost',
        'database': 'turismo'
    }

    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
