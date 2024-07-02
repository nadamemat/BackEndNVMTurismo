import mysql.connector

def get_db_connection():
    config = {
        'user': 'root',
        'password': '123Queso!',
        'host': 'localhost',
        'database': 'turismo'
    }

    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
        else:
            print("La conexión a la base de datos falló")
            return None
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db = cursor.fetchone()
        print(f"Conectado a la base de datos: {db[0]}")
        cursor.close()
        connection.close()
        print("La conexión a la base de datos ha sido cerrada")
