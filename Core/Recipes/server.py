"""Configuración del servidor."""

# App
from app import app

# Controllers
from app.controllers.accounts import *  # noqa: F403
from app.controllers.recipes import *  # noqa: F403


# Run
if __name__ == "__main__":
    app.run(debug=True, port=5001)
