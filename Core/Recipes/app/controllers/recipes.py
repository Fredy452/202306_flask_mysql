# Importando app
from app import app

# flask
from flask import redirect, render_template, session, request, flash, url_for


# Import Model 
from app.models.recipe import Recipe

# Creating routes for dashboard
@app.route('/recipes/')
def recipes():
    """
    Funcion de vista `dashboard`
    """
    # Protegiendo ruta
    if not session.get("user"):
        return redirect('/')
    
    # Obtenemos todas las recetas
    recipes = Recipe.get_recipe_whit_user()
    # for recipe in recipes:
    #     print(recipe)

    
    return render_template('recipes/index.html', recipes=recipes)

@app.route('/logout/')
def logout():
    """
    Funcion de vista cerrar sesion
    """
    session.clear()

    return redirect('/')

@app.route('/recipes/new/')
def recipes_new():
    """
    Funcion de vista recipes nex
    """

    return render_template('recipes/create.html')

@app.route('/recipes/create/', methods=['POST'])
def recipes_create():
    """
    Funcion de vista crear recipes
    """

    # Generamos dictionary
    data = {
        "user_id": session["user"]["id"],
        "first_name": session["user"]["first_name"],
        "title": request.form['title'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "date": request.form['date'],
        "under": request.form['under'],
    }

    # Enviamos data para validar 
    errors = Recipe.validar_recipe(data)

    if len(errors) > 0:
        for error in errors:
            print(error)
            flash(error, 'danger')
            
        return redirect(url_for('recipes_new'))

    # Si no hay eror creamos el objeto
    recipe = Recipe.create(data)

    # Manejando exepciones
    if recipe:
        flash("Receta creada con exito", "success")
    else:
        flash("Ha ocurrido algun error", "danger")

    return redirect(url_for('recipes'))

# Creamos una ruta mostrar recipes
@app.route('/recipe/<int:id>/')
def recipe_show(id):
    """
    Funcion de vista mostrar
    """
    # Obtenemos la receta que recibimos por id
    data = {
        "id": id
    }
    recipe = Recipe.get_one(data)
    
    return render_template("recipes/show.html", recipe=recipe)


# Creamos una ruta editar recipes
@app.route('/recipe/edit/<int:id>/')
def recipe_edit(id):
    """
    Funcion de vista mostrar
    """
    # Obtenemos la receta que recibimos por id
    data = {
        "id": id
    }
    recipe = Recipe.get_one(data)
    

    return render_template("recipes/edit.html", recipe=recipe)

@app.route('/recipe/edit_proccess/<int:id>/', methods=['POST'])
def recipe_edit_proccess(id):
    """
    Funcion de vista editar
    """
    # Generamos dictionary
    data = {
        "id": id,
        "user_id": session["user"]["id"],
        "title": request.form['title'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "date": request.form['date'],
        "under": request.form['under'],
    }
    # Primero validamos
    errors = Recipe.validar_recipe(data)
    if len(errors) > 0:
        for error in errors:
            print(error)
            flash(error, 'danger')
    

    # Si no hay eror creamos el objeto
    Recipe.update(data)
    flash("Receta editada con exito", "success")


    return redirect(url_for('recipes'))

@app.route('/recipe/delete/<int:id>')
def recipe_delete(id):
    """
    Funcion de viata para eliminar receta
    """
    
    data = {
        "id": id
    }
    recipes = Recipe.get_recipe_whit_user()
    for recipe in recipes:
        # Solo el usuario que creó la receta puede eliminarla
        if session["user"]["id"] == recipe["user_id"]:
            flash("La receta fue eliminada", "success")
            Recipe.delete(data)
            return redirect(url_for("recipes"))
    
    flash("No tienes permiso para eliminar la receta", "danger")

    return redirect(url_for('recipes'))
