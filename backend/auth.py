from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup() -> str:
    ''' valide et enregistre les données d'un nouvel utilisateur
    dans la base de données
    '''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # si un utilisateur est retourné, alors l'email existe déjà dans la BD
        user = User.query.filter_by(email=email).first()

        # si un utilisateur est trouvé, on le ramène sur la page d'inscription pour un nouvel essai
        if user:
            flash('Cet utilisateur est déjà inscrit')
            return redirect(url_for('auth.signup_get'))

            # créons un nouvel utilisateur avec les données du formulaire et hashons le mot de passe
        new_user = User(email=email, password=generate_password_hash(
            password, method='sha256'))

        # ajoute le nouvel utilisateur dans la BD
        db.session.add(new_user)
        print("créé")
        db.session.commit()

        # une fois inscrit, le nouvel utilisateur est redirigé sur la page de connexion
        return redirect(url_for('auth.login'))

    # affiche la page d'inscription pour un nouvel utilisateur
    return render_template('signup.html', title='Inscription')


@auth.route('/login', methods=['GET', 'POST'])
def login() -> str:
    ''' assure la connexion d'un utilisateur
    '''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        # vérifie si l'utilisateur existe déjà
        # on compare le mot de passe du formulaire à celui qui est inscrit dans la BD
        if not user or not check_password_hash(user.password, password):
            flash('Identifiants incorrects. Réessayez svp !')
            # si les identifiants sont incorrects, il est amené à réessayer
            return redirect(url_for('auth.login'))

        # si tout se passe bien, il peut maintenant se connecter à la plateforme
        print("connecté youpi")
        login_user(user, remember=True)
        return redirect(url_for('main.index'))

    # affichage de la page de connexion
    return render_template('login.html', title='Connexion')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
