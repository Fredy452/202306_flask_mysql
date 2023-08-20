"""Configuración del servidor."""

# App
from app import app

# Controllers
from app.controllers.books import *  # noqa: F403
from app.controllers.authors import *  # noqa: F403



# Run
if __name__ == "__main__":
    app.run(debug=True, port=5001)