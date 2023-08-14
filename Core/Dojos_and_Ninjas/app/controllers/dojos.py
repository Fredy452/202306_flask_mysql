"""Dojo Controllers"""
# Import
from app import app

# Flask
from flask import redirect, render_template, request

# Models 
from app.models.dojos import Dojo
from app.models.ninjas import Ninja

@app.route('/dojos/')
def dojo():
    """
    Funcion de vista `dojo`
    """

    # Obtenemos todos los dojos para mostrar
    dojos = Dojo.get_all()

    return render_template('dojos/dojo.html', dojos=dojos)


@app.route('/dojo/create/', methods=['POST'])
def dojo_create():
    """
    Funcion de vista crear `create`
    """
    # Asignamos a data el valor del campo nombre
    data = {
        "nombre": request.form['nombre']
    }

    Dojo.create(data)

    return redirect('/dojos/')


@app.route('/dojo/<int:id>')
def dojo_id(id):
    """
    Funcion de vista para mostrar los ninjas que pertenecen a un dojo
    """
    # Agregamos a data el id recibido por parametro
    data = {
        "id": id
    }

    # Enviamos data para consultar los ninjas
    ninjas = Ninja.get_ninjas(data)
    
    # Obtenemos el dojo 
    dojo = Dojo.get_one(data)

    return render_template('dojos/dojo_show.html', ninjas=ninjas, dojo=dojo)