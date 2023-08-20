"""Books Controllers"""
# Import
from app import app

# Flask
from flask import redirect, render_template, request

# Models 
from app.models.books import Book


# Configurando rutas 
@app.route('/books/')
def books():
    """
    Renderiza una vista con la lista de libros.

    Returns:
        str: HTML renderizado con la lista de libros.
    """
    print(Book.get_all())
    return render_template('books/books.html', books = Book.get_all())


@app.route('/books/create/', methods=['POST'])
def book_create():
    """
    Crea un nuevo `Book`.

    Returns:
        redirect: Redirige a la página books después de crear el `book`.
    """
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }

    Book.create(data)

    return redirect('/books/')


@app.route('/book/<int:id>/show')
def book_show(id):
    """
    Funcion de vista mostrar libros
    """
    pass