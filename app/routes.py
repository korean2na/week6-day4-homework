from app import app
from flask import render_template
from app.models import User, Car

@app.route('/')
def home():
    return render_template('home.html.j2')

@app.route('/login')
def login():
    return render_template('login.html.j2')

@app.route('/register')
def register():
    return render_template('register.html.j2')

@app.route('/about')
def about():
    return render_template('about.html.j2')

@app.route('/blog')
def blog():
    return render_template('blog.html.j2')

@app.route('/cars')
def cars():
    car_data = Car.query.all()
    return render_template('cars.html.j2', car_data = car_data)
    # not quite working yet, but it's at least showing Car 1 and Car 2 without error
