# Importing Re

import re

NAME_REGEX = re.compile(r"^[A-Za-z\s']{2,}$")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$")

# Validating recipes
TITLE_REGEX = re.compile(r"^[A-Za-z\s']{3,}$")

# Regex para validar la descripción
DESCRIPTION_REGEX = re.compile(r".{5,}$")

# Regex para validar las instrucciones
INSTRUCTION_REGEX = re.compile(r".{5,}$")

# Regex para validar "Menos de 30 minutos"
UNDER_REGEX = re.compile(r"^(0|1)$", re.IGNORECASE)