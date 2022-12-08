from . import bp
from app import db
from flask import render_template, request, redirect, url_for
from app.models import User, Car

@bp.route('/cars')
def cars():
    car_data = Car.query.all()
    return render_template('cars.html.j2', cars=car_data)

@bp.route('/cars/<id>')
def post_by_id(id):
    car = Car.query.get(id)
    return render_template('post-single.html.j2', car=car)

@bp.route('/list_car', methods=['POST'])
def list_car():
    make = request.form['inputMake']
    model = request.form['inputModel']
    year = request.form['inputYear']
    color = request.form['inputColor']
    price = request.form['inputPrice']
    new_car = Car(make=make, model=model, year=year, color=color, price=price, user_id=1)
    db.session.add(new_car)
    db.session.commit()
    return redirect(url_for('api.cars'))
