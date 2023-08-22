# Import flask
from flask import Flask, render_template, request, session

app = Flask(__name__)


# Key secret
app.secret_key = "password"


# Ruta principal
@app.route('/')
def inicio():
    """
    Función para mostrar el formulario
    """
    return render_template('encuesta.html')


@app.route('/precess/', methods=['POST'])
def process():
    """
    Fucion para guardar los datos en cache
    """
    session['nombre'] = request.form['name']
    session['ubicacion'] = request.form['location']
    session['lenguaje'] = request.form['language']
    session['comentarios'] = request.form['comments']

    print(request.form)
    return render_template('datos.html')



# Creando punto de arranque
if __name__=="__main__":
    app.run(debug=True)