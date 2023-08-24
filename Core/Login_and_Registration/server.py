"""Configuración del servidor."""

# App
from app import app

# Controllers
from app.controllers.login import *  # noqa: F403


# Run
if __name__ == "__main__":
    app.run(debug=True, port=5000)