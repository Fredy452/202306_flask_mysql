"""Email model."""

# Config
from flask import flash
from app.config.mysql_connection import connect_to_mysql

# import
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:
    """Modelo de la clase `User`."""

    def __init__(self, data: dict) -> None:
        """Constructor de la clase `Email`."""

        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    # Validando correo
    @staticmethod
    def validate_email( email ):
        """
        Funcion para validar email
        """
        is_valid = True
        
        # validamos si el formato de email recivido es correcto
        if not EMAIL_REGEX.match(email['email']):
            flash("Ha ocurrido un error", 'danger')
            is_valid = False
        
        flash("Guardado exitosamente", 'success')
        return is_valid

    @classmethod
    def get_all(cls):
        """
        Funcion para obtener todos los emails
        """
        query = """
        select * from emails;
        """
        results = connect_to_mysql().query_db(query)

        # Creamos un objeto iterable de la clase email
        emails: list = []
        for email in results:
            emails.append(cls(email))
        return emails

    @classmethod
    def create(cls, data: dict):
        """Guardar registro de email."""

        query = """
        INSERT INTO emails (email)
        VALUES (%(email)s);
        """
        return connect_to_mysql().query_db(query, data)