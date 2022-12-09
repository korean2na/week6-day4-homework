from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # cars = db.relationship('Car', backref='user')

    def hash_my_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_my_password(self, password):
        return check_password_hash(self.password, password)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref='car')
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# # # Used in flask shell to run a sweep to hash passwords
# def hash_passwords():
#     users = User.query.filter(User.id <= 6).all()
#     for user in users:
#         user.hash_my_password(user.password)
#         db.session.add(user)

#     db.session.commit()