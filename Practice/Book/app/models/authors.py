"""Authors models."""

# Config
from app.config.mysql_connection import connectToMySQL


class Author:
    """Modelo de la clase author."""

    def __init__(self, data: dict) -> None:
        """
        Constructor de la clase `author`.

        El constructor define los atributos `id`, `name`, `created_at`,
        `updated_at`.

        Parámetros:
            - self (object): Objeto de tipo `author`.
            - data (dict): Diccionario con los datos del formulario.
        
        Retorno:
            None: Retorna nada.
        """

        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data.get("created_at", None)
        self.updated_at = data.get("updated_at", None)

    @classmethod
    def get_all(cls):
        """
        Obtener todas las authors de la tabla `author`.
        
        El método `get_all` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `author` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `author`.

        Retorno:
            - author (list): Lista de authors.
        """

        query = """SELECT * FROM authors;"""
        results = connectToMySQL("books").query_db(query)

        # Creamos un objeto iterable de la clase author
        authors: list = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_one(cls, data: dict):
        """
        Obtener un author por id.

        El método `get_one` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `author` sin necesidad de
        crear una instancia (objeto).
        """

        query = """SELECT * FROM authors WHERE id = %(id)s;"""
        result = connectToMySQL("books").query_db(query, data)
        return cls(result[0])

    @classmethod
    def create(cls, data: dict):
        """
        Crear un nuevo author.

        El método `create` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `author` sin necesidad de
        crear una instancia (objeto).

        Ejemplo: author.create({"name": "Joe Doe", "comment": "This is a comment"})

        Parámetros:
            - cls (object): Objeto de tipo `author`
            - data (dict): Diccionario con los datos del author.

        Retorno:
            -
        """

        query = """INSERT INTO authors (name) VALUES (%(name)s);"""  # noqa: E501
        return connectToMySQL("books").query_db(query, data)
    

    @classmethod
    def update(cls, data: dict):
        """
        Metodo para editar un author

        Parámetros:
            - cls (object): Objeto de tipo `author`
            - data (dict): Diccionario con los datos a actualizar.

        Retorno:
            -
        """

        query = """
                    UPDATE authors SET 
                    name = %(name)s 
                    WHERE id = %(id)s;
                """  # noqa: E501
        return connectToMySQL("books").query_db(query, data)
    

    @classmethod
    def delete(cls, data: dict):
        """
        Eliminar author.

        El método `delete` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `author` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `author`
            - data (dict): Diccionario con el id a eliminar

        Retorno:
            -
        """

        query = """DELETE FROM authors where id = %(id)s;"""  # noqa: E501
        return connectToMySQL("books").query_db(query, data)
    
    @classmethod
    def add_favorite_book(cls, data: dict):
        """
         Agrega un libro favorito a un autor.

        Args:
            data (dict): Un diccionario que contiene los datos necesarios para la inserción.
                         Debe contener 'author_id' (ID del autor) y 'book_id' (ID del libro).

        Returns:
            int: El ID de la fila insertada en la tabla de favoritos.

        Raises:
            Exception: Si ocurre un error durante la inserción en la base de datos.
        """  # noqa: E501
        query = """
        INSERT INTO favorites (author_id, book_id)
        VALUES (%(author_id)s, %(book_id)s);
        """
        return connectToMySQL("books").query_db(query, data)
    

    @classmethod
    def get_favorite_book(cls, data: dict):
        """
         Obtiene la lista de los libros favoritos de un author.

        Args:
            data (dict): Un diccionario que contiene el id del author.

        Returns:
            list: Una lista de los libros.

        Raises:
            Exception: Si ocurre un error durante la inserción en la base de datos.
        """  # noqa: E501
        query = """
                select * 
                from books
                left join favorites on favorites.book_id = books.id
                left join authors on authors.id = favorites.author_id
                where authors.id = %(id)s;
        """
        return connectToMySQL("books").query_db(query, data)
