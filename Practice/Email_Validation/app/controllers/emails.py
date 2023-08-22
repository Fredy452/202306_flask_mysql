# Import app
from app import app

# flask
from flask import redirect, render_template, request, url_for

# models
from app.models.emails import Email

# Creating routes
@app.route('/')
def index():
    """
    Funcion de vista principal
    """
    #Yo qiero mostrar los correos solo cuando se procesa el email
    emails = Email.get_all()
    
    return render_template("email.html", emails=emails)


@app.route('/email/proccess/', methods=['POST'])
def email_proccess():
    """
    Funcion de vista para procesar y validar email
    """

    if  not Email.validate_email(request.form):
        return redirect('/')
    
    data = {
        "email": request.form['email']
    }
    Email.create(data)
    
    return redirect( url_for('index'))