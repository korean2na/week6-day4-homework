from . import bp
from app.blueprints.blog.models import User
from app import db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html.j2')

    email = request.form['email']
    password = request.form['password']
    next_url = request.form['next']

    user = User.query.filter_by(email=email).first()

    if user is None:
        flash(f'An account with email "{email}" does not exist.', 'danger')

    elif user.check_my_password(password):
        login_user(user)
        flash(f'Welcome back, {user.username}!', 'success')
        
        if next_url != '':
            return redirect(next_url)

        return redirect(url_for('main.home'))

    else:
        flash('Password was incorrect.', 'danger')

    return render_template('login.html.j2')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html.j2')

    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']
    username = request.form['username']
    first_name = request.form['firstName']
    last_name = request.form['lastName']

    check_email = User.query.filter_by(email=email).first()
    check_username = User.query.filter_by(username=username).first()

    if check_email is not None:
        flash(f'An account with email address "{email}" already exists.', 'danger')

    elif check_username is not None:
        flash(f'An account with username "{username}" already exists.', 'danger')
    
    elif password != confirm_password:
        flash('Password and Confirm Password did not match.', 'danger')

    else:
        try:
            new_user = User(email=email, username=username, password='', first_name=first_name, last_name=last_name)
            new_user.hash_my_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Account "{new_user.username}" created successfully!', 'success')
            return redirect(url_for('auth.login'))
        except:
            flash('There was an error.', 'danger')

    return render_template('register.html.j2')

@bp.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('auth.login'))

@bp.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'GET':
        return render_template('reset-password.html.j2')

    old_password = request.form['oldPassword']
    new_password = request.form['newPassword']
    confirm_new = request.form['confirmNew']

    if not current_user.check_my_password(old_password):
        flash('Old password was incorrect.', 'danger')

    elif confirm_new != new_password:
        flash('New Password and Confirm New Password did not match.', 'danger')

    else:
        current_user.hash_my_password(new_password)
        db.session.add(current_user)
        db.session.commit()
        flash('Password changed successfully!', 'success')

    return render_template('reset-password.html.j2')