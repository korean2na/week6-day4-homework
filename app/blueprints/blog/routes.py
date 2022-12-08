from . import bp
from flask import render_template

@bp.route('/blog')
def blog():
    return render_template('blog.html.j2')