"""dojo models."""

# Config
from app.config.mysql_connection import connectToMySQL


class Dojo:
    """Modelo de la clase dojo."""

    def __init__(self, data: dict) -> None:
        """
        Constructor de la clase `dojo`.

        El constructor define los atributos `id`, `nombre`, `created_at`,
        `updated_at`.

        Parámetros:
            - self (object): Objeto de tipo `dojo`.
            - data (dict): Diccionario con los datos de la usuario.
        
        Retorno:
            None: Retorna nada.
        """

        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data.get("created_at", None)
        self.updated_at = data.get("updated_at", None)

    @classmethod
    def get_all(cls):
        """
        Obtener todas las dojos de la tabla `dojo`.
        
        El método `get_all` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `dojo` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `dojo`.

        Retorno:
            - dojo (list): Lista de dojos.
        """

        query = """SELECT * FROM dojos;"""
        results = connectToMySQL("dojos_y_ninjas").query_db(query)

        # Creamos un objeto iterable de la clase dojo
        dojos: list = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, data: dict):
        """
        Obtener un dojo por id.

        El método `get_one` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `dojo` sin necesidad de
        crear una instancia (objeto).
        """

        query = """SELECT * FROM dojos WHERE id = %(id)s;"""
        result = connectToMySQL("dojos_y_ninjas").query_db(query, data)
        return cls(result[0])

    @classmethod
    def create(cls, data: dict):
        """
        Crear un nuevo usuario.

        El método `create` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `dojo` sin necesidad de
        crear una instancia (objeto).

        Ejemplo: dojo.create({"name": "Joe Doe", "comment": "This is a comment"})

        Parámetros:
            - cls (object): Objeto de tipo `dojo`
            - data (dict): Diccionario con los datos de la usuario.

        Retorno:
            -
        """

        query = """INSERT INTO dojos (nombre) VALUES (%(nombre)s);"""  # noqa: E501
        return connectToMySQL("dojos_y_ninjas").query_db(query, data)
    

    @classmethod
    def update(cls, data: dict):
        """
        Metodo para editar un dojo

        Parámetros:
            - cls (object): Objeto de tipo `dojo`
            - data (dict): Diccionario con los datos a actualizar.

        Retorno:
            -
        """

        query = """
                    UPDATE dojos SET 
                    nombre = %(nombre)s 
                    WHERE id = %(id)s;
                """  # noqa: E501
        return connectToMySQL("dojos_y_ninjas").query_db(query, data)
    

    @classmethod
    def delete(cls, data: dict):
        """
        Eliminar dojo.

        El método `delete` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `dojo` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `dojo`
            - data (dict): Diccionario con el id a eliminar

        Retorno:
            -
        """

        query = """DELETE FROM dojos where id = %(id)s;"""  # noqa: E501
        return connectToMySQL("dojos_y_ninjas").query_db(query, data)
