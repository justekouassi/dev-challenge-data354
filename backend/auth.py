from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup_get() -> str:
    ''' affiche la page d'inscription pour un nouvel utilisateur
    '''
    return render_template('signup.html', title='Inscription')


@auth.route('/signup', methods=['POST'])
def signup_post() -> str:
    ''' valide et enregistre les données d'un nouvel utilisateur
    dans la base de données
    '''
    email = request.form.get('email')
    password = request.form.get('password')

    # si un utilisateur est retourné, alors l'email existe déjà dans la BD
    user = User.query.filter_by(email=email).first()

	# si un utilisateur est trouvé, on le ramène sur la page d'inscription pour un nouvel essai
    if user:
        return redirect(url_for('auth.signup_get'))

	# créons un nouvel utilisateur avec les données du formulaire et hashons le mot de passe
    new_user = User(email=email, password=generate_password_hash(
        password, method='sha256'))

    # ajoute le nouvel utilisateur dans la BD
    db.session.add(new_user)
    print("créé")
    db.session.commit()
    
    return redirect(url_for('auth.login')) # redirige sur la page de connexion


@auth.route('/login', methods=['GET', 'POST'])
def login() -> str:
    ''' assure la connexion d'un utilisateur
    '''
    return render_template('login.html', title='Connexion')


@auth.route('/logout')
def logout():
    return 'Logout'
