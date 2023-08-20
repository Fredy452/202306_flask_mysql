"""Dojo Controllers"""
# Import
from app import app

# Flask
from flask import redirect, render_template, request, url_for

# Models 
from app.models.authors import Author
from app.models.books import Book


# Configurando rutas 
@app.route('/')
def authors():
    """
    Renderiza una vista con la lista de autores.

    Returns:
        str: HTML renderizado con la lista de autores.
    """
    
    return render_template('authors/authors.html', authors = Author.get_all())


@app.route('/authors/create/', methods=['POST'])
def author_create():
    """
    Crea un nuevo autor.

    Returns:
        redirect: Redirige a la página principal después de crear el autor.
    """
    data = {
        "name": request.form['name']
    }

    Author.create(data)

    return redirect('/')


@app.route('/favorite/<int:id>/create', methods=['POST'])
def favorite_create(id):
    """
    docstring
    """
    data = {
        "author_id": id,
        "book_id": request.form['book_id']
    }

    Author.add_favorite_book(data)
    return redirect(url_for("autor_favorites", id=id))

@app.route('/authors/<int:id>/favorites')
def autor_favorites(id):
    """
    docstring
    """
    data = {
        "id": id
    }
    favorites = Author.get_favorite_book(data)

    return render_template('authors/favorites.html',favorites = favorites, author = Author.get_one(data), books = Book.get_all())  # noqa: E501 