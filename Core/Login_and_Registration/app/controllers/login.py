# Import app 
from app import app

# Flask libraries
from flask import flash, redirect, render_template, request, url_for, session


# Import models
from app.models.users import User

# Bcrypt app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#creating routes
@app.route('/')
def index():
    """
    Funcion de vista de `index`
    """
    
    return render_template('login/login.html')


@app.route('/register/', methods=['POST'])
def register():
    """
    Funcion de vista para procesar el registro
    """
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password']
    }

    errores = User.valida_user(data)

    if len(errores) > 0:
        for error in errores:
            print(error)
            flash(error, 'danger')
            
        return redirect('/')
    # Verificamos si existe un usuario para crear
    user = User.get_by_email(data)

    if user:
        flash("Vuelve a intentar", 'danger')
        return redirect('/')

    if data['password'] != request.form['confirm_password']:
        flash("Las contraseñas no coinciden", "danger")
        return redirect('/')

    password_hash = bcrypt.generate_password_hash(data['password'])
    data['password'] = password_hash
    User.create(data)
    flash("Usuario creado correctamente", "success")
    return redirect('/')

@app.route('/login/', methods=['POST'])
def login():
    """
    Funcion de vista de `login`
    """
    password = request.form['password']

    data = {"email": request.form['email']}
    user = User.get_by_email(data)

    if not user:
        flash("Usuario no registrado", "danger")
        return redirect('/')
    
    check_password = bcrypt.check_password_hash(user.password, password)
    if check_password:
        session["user"] = {
            "id": user.id,
            "email": user.email
        }
        flash("Genial, pudiste iniciar sesión", "info")
    else:
        flash("Error", "danger")
        return redirect(url_for("index"))

    return redirect(url_for("dashboard"))


@app.route('/dashboard/')
def dashboard():
    """
    Funcion de vista principal 
    """
    user = session.get('user')  # Obtén el usuario de la sesión

    if not user:  # Verifica si no hay un usuario en la sesión
        return redirect('/')

    return render_template('dashboard/inicio.html')

@app.route('/logout/')
def logout():
    """
    Función de vista para cerrar sesión
    """
    session.clear()

    return redirect('/')
