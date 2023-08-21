"""User model."""

# Config
from app.config.mysql_connection import connect_to_mysql


class User:
    """Modelo de la clase `User`."""

    def __init__(self, data: dict) -> None:
        """Constructor de la clase `User`."""

        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """Obtener todos los friends"""

        query = """
            select * from users;
        """
        results = connect_to_mysql().query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        
        return users

    @classmethod
    def create(cls, data: dict):
        """Guardar registro de usuario."""

        query = """
        INSERT INTO users (first_name, last_name)
        VALUES (%(first_name)s, %(last_name)s);
        """
        return connect_to_mysql().query_db(query, data)