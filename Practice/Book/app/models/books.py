"""Book models."""

# Config
from app.config.mysql_connection import connectToMySQL


class Book:
    """Modelo de la clase book."""

    def __init__(self, data: dict) -> None:
        """
        Constructor de la clase `book`.

        El constructor define los atributos `id`, `title`, `num_of_pages`, `created_at`,
        `updated_at`.

        Parámetros:
            - self (object): Objeto de tipo `book`.
            - data (dict): Diccionario con los datos del formulario.
        
        Retorno:
            None: Retorna nada.
        """

        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data.get("created_at", None)
        self.updated_at = data.get("updated_at", None)

    @classmethod
    def get_all(cls):
        """
        Obtener todas las books de la tabla `book`.
        
        El método `get_all` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `book` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `book`.

        Retorno:
            - book (list): Lista de books.
        """

        query = """SELECT * FROM books;"""
        results = connectToMySQL("books").query_db(query)

        # Creamos un objeto iterable de la clase book
        books: list = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def get_one(cls, data: dict):
        """
        Obtener un book por id.

        El método `get_one` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `book` sin necesidad de
        crear una instancia (objeto).
        """

        query = """SELECT * FROM books WHERE id = %(id)s;"""
        result = connectToMySQL("books").query_db(query, data)
        return cls(result[0])

    @classmethod
    def create(cls, data: dict):
        """
        Crear un nuevo book.

        El método `create` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `book` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `book`
            - data (dict): Diccionario con los datos del book.

        Retorno:
            -
        """

        query = """INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"""  # noqa: E501
        return connectToMySQL("books").query_db(query, data)
    

    @classmethod
    def update(cls, data: dict):
        """
        Metodo para editar un book

        Parámetros:
            - cls (object): Objeto de tipo `book`
            - data (dict): Diccionario con los datos a actualizar.

        Retorno:
            -
        """

        query = """
                    UPDATE books SET 
                    title = %(title)s 
                    num_of_pages = %(num_of_pages)s 
                    WHERE id = %(id)s;
                """  # noqa: E501
        return connectToMySQL("books").query_db(query, data)
    

    @classmethod
    def delete(cls, data: dict):
        """
        Eliminar book.

        El método `delete` es un método de clase, lo que significa que se
        puede llamar directamente desde la clase `book` sin necesidad de
        crear una instancia (objeto).

        Parámetros:
            - cls (object): Objeto de tipo `book`
            - data (dict): Diccionario con el id a eliminar

        Retorno:
            -
        """

        query = """DELETE FROM books where id = %(id)s;"""  # noqa: E501
        return connectToMySQL("books").query_db(query, data)
