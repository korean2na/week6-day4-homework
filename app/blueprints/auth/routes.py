from . import bp
from flask import render_template

@bp.route('/login')
def login():
    return render_template('login.html.j2')

@bp.route('/register')
def register():
    return render_template('register.html.j2')