"""MySQL connection."""

# PyMySQL
import pymysql.cursors


class MySQLConnection:
    """Clase modelo MySQL connection."""

    def __init__(self, db):
        """
        Constructor encargado de crear un objeto de tipo MySQLConnection.
        El constructor recibe el nombre de la base de datos a la que se desea conectar.

        Parámetros:
            - self: Es una referencia a la instancia de la clase.
            - db: Nombre de la base de datos.

        Retorno:
            - None: No retorna nada.
        """
        connection = pymysql.connect(
            host = "localhost",  # Cambiar por el host de la base de datos.
            user = "root",  # Cambiar por el usuario de la base de datos.
            password = "root",  # Cambiar por la contraseña de la base de datos.
            db = db,  # Nombre de la base de datos.
            charset = "utf8mb4",  # Codificación de caracteres.
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True  # Auto commit.
        )
        self.connection = connection
    
    def query_db(self, query, data=None):
        """
        Query DB.
        El método `query_db()` es el encargado de ejecutar las consultas a la base de datos.

        Parámetros:
            - self: Es una referencia a la instancia de la clase.
            - query: Consulta a la base de datos.
            - data: Datos a insertar en la consulta.

        Retorno:
            - False: En caso de que la consulta falle.
        """
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print(f"Running Query: {query}")
                executable = cursor.execute(query, data)

                if query.lower().find("insert") >= 0:
                    # Si la consulta es un insert, retorna el id del registro insertado.
                    # El resultado de la consulta es el id del registro insertado.
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # Si la consulta es un select, retorna los registros encontrados.
                    # El resultado de la consulta es una lista de diccionarios.
                    result = cursor.fetchall()
                    return result
                else:
                    # Si la consulta es un update o un delete, no retorna nada.
                    self.connection.commit()
            except Exception as e:
                # En caso de que la consulta falle, retorna False.
                print(f"Something went wrong {e}")
                return False
            finally:
                # Cerrar la conexión a la base de datos.
                self.connection.close()


def connect_to_mysql(db):
    """
    Connect to MySQL.
    La función `connectToMySQL()` es la encargada de crear una instancia de la clase MySQLConnection, 
    la cual será utilizada por el servidor (server.py).

    Parámetros:
        - db: Nombre de la base de datos.

    Retorno:
        - MySQLConnection: Instancia de la clase MySQLConnection.
    """
    return MySQLConnection(db)
