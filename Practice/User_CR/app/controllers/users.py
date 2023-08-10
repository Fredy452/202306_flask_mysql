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

    #Creamos un adata para asignarle los valores de request.form
    # data = {
    #     "first_name": request.form["first_name"],
    #     "last_name": request.form["last_name"],
    #     "email": request.form["email"]
    # }
    # print(request.form)

    # Enviamos data al metodo de la clase de User.create
    #User.create(data)

    # Una ves que enviamos redireccionamos al home
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

@app.route("/user/prueba")
def prueba():
    """Función de vista `new user`."""
    return "Hello"


# Creando punto de arranque
if __name__=="__main__":
    app.run(debug=True)