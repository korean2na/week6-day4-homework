from . import bp
from app import db
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.blog.models import User, Car
from flask_login import current_user, login_required

@bp.route('/posts')
def posts():
    return render_template('posts.html.j2')

@bp.route('/cars')
def cars():
    car_data = Car.query.all()
    return render_template('cars.html.j2', cars=car_data)

@bp.route('/users_cars')
@login_required
def users_cars():
    cars = Car.query.filter_by(user_id=current_user.id).all()
    return render_template('users-cars.html.j2', cars=cars)

@bp.route('/cars/id/<id>')
def car_by_id(id):
    car = Car.query.get(id)
    return render_template('car-by-id.html.j2', car=car)

@bp.route('/cars/username/<username>')
def cars_by_owner(username):
    target = User.query.filter_by(username=username).first()
    cars = Car.query.filter_by(user_id=target.id).all()
    return render_template('cars-by-owner.html.j2', target=target, cars=cars)

@bp.route('/list_your_car')
def list_your_car():
    return render_template('new-car.html.j2')

@bp.route('/list_car', methods=['POST'])
def list_car():
    make = request.form['inputMake']
    model = request.form['inputModel']
    year = request.form['inputYear']
    color = request.form['inputColor']
    price = request.form['inputPrice']
    new_car = Car(make=make, model=model, year=year, color=color, price=price, user_id=current_user.id)
    db.session.add(new_car)
    db.session.commit()
    flash('Car listing created successfully!', 'success')
    return redirect(url_for('blog.users_cars'))
