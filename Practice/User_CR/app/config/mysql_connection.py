"""MySQL connection."""

# PyMySQL
import pymysql.cursors


class MySQLConnection:
    """Clase modelo MySQLConnection."""

    def __init__(self, db):
        """
        Constructor encargado de crear un objeto de tipo `MySQLConnection`.
        El constructor recibe el nombre de la base de datos a la que se desea
        conectar.
        
        Parámetros:
            - self: Es un referencia a la instancia de la clase.
            - db (str): Nombre del esquema o base de datos.

        Retorno:
            - None: Retorna nada.
        """

        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "8446_tigo", 
            db = db,
            charset = "utf8mb4",
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True
        )
        self.connection = connection

    def query_db(self, query, data=None):
        """
        El método `query_db` es el encargado de ejecutar las consultas a la
        base de datos (esquema).

        Parámetros:
            - self: Es una referencia a la instancia de la clase.
            - query: Consulta SQL a la base de datos (esquema).
            - data: Datos a insertar en la consulta.

        Retorno:
            - False (bool): En caso que la consulta falle. 
        """
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                executable = cursor.execute(query, data)  # noqa: F841
                if query.lower().find("insert") >= 0:
                    # if the query is an insert, return the id of the last row, since that is the row we just added  # noqa: E501
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # if the query is a select, return everything that is fetched from the database  # noqa: E501
                    # the result will be a list of dictionaries
                    result = cursor.fetchall()
                    return result
                else:
                    # if the query is not an insert or a select, such as an update or delete, commit the changes  # noqa: E501
                    # return nothing
                    self.connection.commit()
            except Exception as e:
                # in case the query fails
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 


def connectToMySQL(db):
    """
    La función la `connectToMySQL` es la encargada de crear una instancia de
    la clase `MySQLConnection`, la cual será utilizada por el servidor.

    Parámetros:
        - db (str): Nombre del esquema o base de datos.

    Retorno:
        - MySQLConnection (class): Instancia de la clase.
    """
    return MySQLConnection(db)
