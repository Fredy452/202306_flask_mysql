"""Users Controllers"""
# Import
from app import app

# Flask
from flask import redirect, render_template, request

# Models 
from app.models.dojos import Dojo

@app.route('/dojos/')
def dojo():
    """
    Funcion de vista `dojo`
    """

    # Obtenemos todos los dojos para mostrar
    dojos = Dojo.get_all()

    return render_template('dojos/dojo.html', dojos=dojos)


@app.route('/dojo/create/', methods=['POST'])
def deojo_create():
    """
    Funcion de vista crear `create`
    """
    # Asignamos a data el valor del campo nombre
    data = {
        "nombre": request.form['nombre']
    }

    Dojo.create(data)

    return redirect('/dojos/')
