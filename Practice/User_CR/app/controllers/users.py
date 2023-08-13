"""Users Controllers"""
# Import
from app import app

# Flask
from flask import redirect, render_template, request

# Models 
from app.models.users import User


@app.route("/")
def home():
    """Función de vista `home`."""

    users = User.get_all()

    return render_template('users/show.html', users=users) 


@app.route("/user/form")
def create():
    """Función de vista `new user`."""
    return render_template("users/create.html")


@app.route("/user/new/", methods=['POST'])
def user_new():
    """Función de vista `new user`."""

    # Creamos un adata para asignarle los valores de request.form
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    print(request.form)

    # Enviamos data al metodo de la clase de User.create
    User.create(data)

    # Una ves que enviamos redireccionamos al home
    return redirect("/")


@app.route("/show/user/<int:id>")
def show_user(id):
    """Función de vista `show user`."""

    data = {
        "id": id
    }
    user = User.get_one(data)

    return render_template('users/user.html', user=user)


@app.route("/user/<int:id>/delete")
def user_delete(id):
    """Función de vista `delete user`."""

    data = {
        "id": id
    }
    User.delete(data)

    return redirect('/')


@app.route("/user/<int:id>/edit")
def user_id_edit(id):
    """Función de vista `edit user`."""

    data = {
        "id": id
    }
    # Obtnemos el usuario con el id recibido
    user = User.get_one(data)

    return render_template('users/edit.html', user=user)


@app.route("/user/edit/", methods=['POST'])
def user_edit():
    """Función de renderizar `edit user`."""

    data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    # Enviamos los datos del usuario a editar
    User.update(data)

    return redirect('/')



# Creando punto de arranque
if __name__=="__main__":
    app.run(debug=True)