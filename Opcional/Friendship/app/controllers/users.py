# Flask
from app import app

#libraries
from flask import redirect, render_template, request, url_for

#Models
from app.models.friend import Friends
from app.models.user import User

@app.route('/friendships/')
def friendships():
    """
    Funcion de vista principal 
    """
    friendships = Friends.get_user_friendship()
    users = User.get_all()

    return render_template('friendships/index.html', friendships=friendships, users=users)  # noqa: E501


@app.route('/user_create/', methods=['POST'])
def user_create():
    """
    Metodo de vista para crear usuarios
    """
    data = {  # noqa: F841
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name']
    }

    User.create(data)
    
    return redirect(url_for('friendships'))


@app.route('/friendship_create/', methods=['POST'])
def friendship_create():
    """
    docstring
    """
    data = {
        "user_id": request.form['user_id'],
        "friend_id": request.form['friend_id']
    }

    Friends.create_friendship(data)

    return redirect(url_for('friendships'))