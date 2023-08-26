"""Recipes models."""

# Config
from app.config.mysql_connection import connect_to_mysql
from app.utils.regular_expresions import TITLE_REGEX, INSTRUCTION_REGEX, DESCRIPTION_REGEX, UNDER_REGEX  # noqa: E501


class Recipe:
    """Modelo de la clase Recipes."""

    def __init__(self, data: dict) -> None:
        """
        Constructor de la clase `recipe`.

        Parámetros:
            - self (object): Objeto de tipo `recipe`.
            - data (dict): Diccionario con los datos de la reseta.
        
        Retorno:
            None: Retorna nada.
        """

        self.id = data["id"]
        self.user_id = data["user_id"]
        self.title = data["title"]
        self.description = data["description"]
        self.instruction = data.get("instruction")
        self.date = data.get("date")
        self.under = data.get("under")
        self.created_at = data.get("created_at", None)
        self.updated_at = data.get("updated_at", None)

    @staticmethod
    def validar_recipe(data):
        """
        Funcion para validar datos recibidos
        """
        errores = []


        if not TITLE_REGEX.match(data['title']):
            errores.append("El titulo al menos tiene que tener tres caracteres")

        if not INSTRUCTION_REGEX.match(data['instruction']):
            errores.append("La instruccion al menos tiene que tener 5 caracters")

        if not DESCRIPTION_REGEX.match(data['description']):
            errores.append("La descripción al menos tiene que tener 5 caracters")

        if not UNDER_REGEX.match(data['under']):
            errores.append("Selecionar yes or no")


        return errores

    @classmethod
    def get_recipe_whit_user(cls):
        """
        Obtener todas las resetas y el usuario de la tabla `recipes`.
        
        El método `get_all` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `recipe` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `recipe`.

        Retorno:
            - recipes (list): Lista de resetas.
        """

        query = """
                SELECT recipes.id, recipes.title, recipes.under, users.first_name, users.id as user_id 
                FROM recipes
                JOIN users ON users.id = recipes.user_id;
        """  # noqa: E501
        results = connect_to_mysql().query_db(query)
        return results

    @classmethod
    def get_one(cls, data: dict):
        """
        Obtener un reseta por id.

        El método `get_one` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `recipe` sin necesidad de
        crear una instancia (objeto).
        """

        query = """SELECT * FROM recipes WHERE id = %(id)s;"""
        result = connect_to_mysql().query_db(query, data)
        return cls(result[0])

    @classmethod
    def create(cls, data: dict):
        """
        Crear una nuevo reseta.

        El método `create` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `recipe` sin necesidad de
        crear una instancia (objeto).


        Parámetros:
            - cls (object): Objeto de tipo `recipe`
            - data (dict): Diccionario con los datos de la reseta.

        Retorno:
            - id 
        """

        query = """INSERT INTO recipes (user_id, title, instruction, description, date, under) VALUES (%(user_id)s, %(title)s, %(instruction)s, %(description)s, %(date)s, %(under)s);"""  # noqa: E501
        return connect_to_mysql().query_db(query, data)
    

    @classmethod
    def update(cls, data: dict):
        """
        Metodo para editar un reseta

        Parámetros:
            - cls (object): Objeto de tipo `recipe`
            - data (dict): Diccionario con los datos a actualizar.

        Retorno:
            -
        """

        query = """
                    UPDATE recipes SET 
                    title = %(title)s, instruction = %(instruction)s, description = %(description)s, date = %(date)s, under = %(under)s, user_id = %(user_id)s
                    WHERE id = %(id)s;
                """  # noqa: E501
        return connect_to_mysql().query_db(query, data)
    

    @classmethod
    def delete(cls, data: dict):
        """
        Eliminar reseta.

        El método `delete` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `recipe` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `recipe`
            - data (dict): Diccionario con el id a eliminar

        Retorno:
            -
        """

        query = """DELETE FROM recipes where id = %(id)s;"""  # noqa: E501
        return connect_to_mysql().query_db(query, data)
