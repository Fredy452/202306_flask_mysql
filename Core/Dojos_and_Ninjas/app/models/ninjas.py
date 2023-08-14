"""Ninja models."""

# Config
from app.config.mysql_connection import connectToMySQL


class Ninja:
    """Modelo de la clase ninjas."""

    def __init__(self, data: dict) -> None:
        """
        Constructor de la clase `Ninja`.

        El constructor define los atributos `id`, `nombre`,`apellido`, `edad`, `dojo_id` `created_at`,
        `updated_at`,.

        Parámetros:
            - self (object): Objeto de tipo `Ninja`.
            - data (dict): Diccionario con los datos de la ninja.
        
        Retorno:
            None: Retorna nada.
        """  # noqa: E501

        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.edad = data.get("edad")
        self.dojo_id = data.get("dojo_id")
        self.created_at = data.get("created_at", None)
        self.updated_at = data.get("updated_at", None)

    @classmethod
    def get_all(cls):
        """
        Obtener todas las ninjas de la tabla `ninjas`.
        
        El método `get_all` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `Ninja` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `Ninja`.

        Retorno:
            - ninjas (list): Lista de ninjas.
        """

        query = """SELECT * FROM ninjas;"""
        results = connectToMySQL("dojos_y_ninjas").query_db(query)

        ninjas: list = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_one(cls, data: dict):
        """
        Obtener un ninja por id.

        El método `get_one` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `Ninja` sin necesidad de
        crear una instancia (objeto).
        """

        query = """SELECT * FROM ninjas WHERE id = %(id)s;"""
        result = connectToMySQL("dojos_y_ninjas").query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_ninjas(cls, data: dict):
        """
        Obtener los ninjas asociados a un dojo por su id.

        Parámetros:
            - cls (object): Objeto de tipo `dojo`.
            - data (dict): Diccionario con el id a consultar.

        Retorno:
            - Ninja (list): Lista de ninjas.
        """
        
        query = """
                    SELECT ninjas.id, ninjas.nombre, ninjas.apellido, ninjas.edad, dojos.id
                    FROM dojos
                    LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
                    WHERE dojos.id = %(id)s;
                """  # noqa: E501
        results = connectToMySQL("dojos_y_ninjas").query_db(query, data)

        ninjas: list = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
        


    @classmethod
    def create(cls, data: dict):
        """
        Crear un nuevo ninja.

        El método `create` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `Ninja` sin necesidad de
        crear una instancia (objeto).

        Ejemplo: Ninja.create({"name": "Joe Doe", "comment": "This is a comment"})

        Parámetros:
            - cls (object): Objeto de tipo `Ninja`
            - data (dict): Diccionario con los datos de la ninja.

        Retorno:
            -
        """

        query = """INSERT INTO ninjas (nombre, apellido, edad, dojo_id) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(dojo_id)s);"""  # noqa: E501
        return connectToMySQL("dojos_y_ninjas").query_db(query, data)
    

    @classmethod
    def update(cls, data: dict):
        """
        Metodo para editar un ninja

        Parámetros:
            - cls (object): Objeto de tipo `Ninja`
            - data (dict): Diccionario con los datos a actualizar.

        Retorno:
            -
        """

        query = """
                    UPDATE ninjas SET 
                    nombre = %(nombre)s, apellido = %(apellido)s, edad = %(edad)s, dojo_id = %(dojo_id)s 
                    WHERE id = %(id)s;
                """  # noqa: E501
        return connectToMySQL("dojos_y_ninjas").query_db(query, data)
    

    @classmethod
    def delete(cls, data: dict):
        """
        Eliminar ninja.

        El método `delete` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `Ninja` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `Ninja`
            - data (dict): Diccionario con el id a eliminar

        Retorno:
            -
        """

        query = """DELETE FROM ninjas where id = %(id)s;"""  # noqa: E501
        return connectToMySQL("dojos_y_ninjas").query_db(query, data)
