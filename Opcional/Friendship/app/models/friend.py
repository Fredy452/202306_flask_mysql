"""Friends model."""

# Config
from app.config.mysql_connection import connect_to_mysql


class Friends:
    """Modelo de la clase `Friends`."""

    def __init__(self, data: dict) -> None:
        """Constructor de la clase `Friends`."""

        self.user = data["user"]
        self.friend = data["friend"]

    @classmethod
    def get_user_friendship(cls):
        """Obtener todos los friends"""

        query = """
            SELECT concat(users.first_name,' ', users.last_name) AS user, 
            concat(user2.first_name,' ',user2.last_name) AS friend
            FROM users
            JOIN friendships ON users.id = friendships.user_id
            JOIN users AS user2 ON user2.id = friendships.friend_id;
        """
        results = connect_to_mysql().query_db(query)
         # Creamos un objeto iterable de la clase dojo
        frienships: list = []
        for frienship in results:
            frienships.append(cls(frienship))
        return frienships


    @classmethod
    def create_friendship(cls, data: dict):
        """Funcion para crear frienships"""
        query = """
                INSERT INTO friendships(user_id, friend_id) VALUES(%(user_id)s, %(friend_id)s);
                """  # noqa: E501
        
        return connect_to_mysql().query_db(query, data)