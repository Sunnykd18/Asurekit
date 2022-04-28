from flask import Blueprint, render_template, session
from . import db
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    # print(current_user)
    # print(current_user.username)
    # print(session)
    # print(session["_user_id"])

    return render_template('profile.html', name=current_user.username)


