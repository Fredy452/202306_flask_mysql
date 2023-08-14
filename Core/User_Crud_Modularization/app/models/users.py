"""Users models."""

# Config
from Core.Dojos_and_Ninjas.app.config.mysql_connection import connectToMySQL


class User:
    """Modelo de la clase Users."""

    def __init__(self, data: dict) -> None:
        """
        Constructor de la clase `user`.

        El constructor define los atributos `id`, `name`, `created_at`,
        `updated_at`, `comment`.

        Parámetros:
            - self (object): Objeto de tipo `user`.
            - data (dict): Diccionario con los datos de la usuario.
        
        Retorno:
            None: Retorna nada.
        """

        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data.get("email")
        self.created_at = data.get("created_at", None)
        self.updated_at = data.get("updated_at", None)

    @classmethod
    def get_all(cls):
        """
        Obtener todas las usuarios de la tabla `users`.
        
        El método `get_all` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `user` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `user`.

        Retorno:
            - users (list): Lista de usuarios.
        """

        query = """SELECT * FROM users;"""
        results = connectToMySQL("users_schema").query_db(query)

        users: list = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data: dict):
        """
        Obtener un usuario por id.

        El método `get_one` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `user` sin necesidad de
        crear una instancia (objeto).
        """

        query = """SELECT * FROM users WHERE id = %(id)s;"""
        result = connectToMySQL("users_schema").query_db(query, data)
        return cls(result[0])

    @classmethod
    def create(cls, data: dict):
        """
        Crear un nuevo usuario.

        El método `create` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `user` sin necesidad de
        crear una instancia (objeto).

        Ejemplo: user.create({"name": "Joe Doe", "comment": "This is a comment"})

        Parámetros:
            - cls (object): Objeto de tipo `user`
            - data (dict): Diccionario con los datos de la usuario.

        Retorno:
            -
        """

        query = """INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"""  # noqa: E501
        return connectToMySQL("users_schema").query_db(query, data)
    

    @classmethod
    def update(cls, data: dict):
        """
        Metodo para editar un usuario

        Parámetros:
            - cls (object): Objeto de tipo `user`
            - data (dict): Diccionario con los datos a actualizar.

        Retorno:
            -
        """

        query = """
                    UPDATE users SET 
                    first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s 
                    WHERE id = %(id)s;
                """  # noqa: E501
        return connectToMySQL("users_schema").query_db(query, data)
    

    @classmethod
    def delete(cls, data: dict):
        """
        Eliminar usuario.

        El método `delete` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `user` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `user`
            - data (dict): Diccionario con el id a eliminar

        Retorno:
            -
        """

        query = """DELETE FROM users where id = %(id)s;"""  # noqa: E501
        return connectToMySQL("users_schema").query_db(query, data)
