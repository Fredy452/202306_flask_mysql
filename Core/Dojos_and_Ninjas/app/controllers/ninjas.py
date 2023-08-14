"""Dojo Controllers"""
# Import
from app import app

# Flask
from flask import redirect, render_template, request

# Models 
from app.models.dojos import Dojo
from app.models.ninjas import Ninja

@app.route('/ninja/')
def ninja():
    """
    Funcion de vista `ninja`
    """

    # Obtenemos todos los dojos para poder enviar al ninja
    dojos = Dojo.get_all()
    
    return render_template('ninjas/create.html', dojos=dojos)


@app.route('/ninja/create/', methods=['POST'])
def ninja_create():
    """
    Funcion de vista create `ninja`
    """
    data = {
        "dojo_id": request.form['dojo_id'],
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "edad": request.form['edad']
    }

    # Enviamos data a la funcion de create ninja
    Ninja.create(data)

    # Una ves creado el ninja hacemos un redirect
    return redirect('/ninja/')