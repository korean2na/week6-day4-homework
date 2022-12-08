from . import bp
from flask import render_template

@bp.route('/')
def home():
    return render_template('home.html.j2')

@bp.route('/about')
def about():
    return render_template('about.html.j2')