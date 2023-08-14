"""Configuración del servidor."""

# App
from app import app

# Controllers
from app.controllers.dojos import *  # noqa: F403
from app.controllers.ninjas import *  # noqa: F403


# Run
if __name__ == "__main__":
    app.run(debug=True, port=5002)