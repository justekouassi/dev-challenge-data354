''' Module d'authentification
'''


from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User, db

# sous-application gérant l'authentification
auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup() -> str:
    ''' valide et enregistre les données d'un nouvel utilisateur
    dans la base de données
    '''
    # si l'utilisateur clique sur le bouton d'inscription
    if request.method == 'POST':
        # on récupère ses données inscrites dans le formulaire
        email = request.form.get('email')
        password = request.form.get('password')

        # et on recherche si l'email existe déjà dans la BD. Alors un objet utilisateur sera retourné
        user = User.query.filter_by(email=email).first()

        # si un utilisateur est trouvé, on le ramène sur la page d'inscription pour un nouvel essai
        if user:
            flash('Cet utilisateur est déjà inscrit')
            return redirect(url_for('auth.signup'))

        # sinon, on crée un nouvel utilisateur avec les données du formulaire tout en hashant le mot de passe
        new_user = User(email=email, password=generate_password_hash(
            password, method='sha256'))

        # puis on ajoute le nouvel utilisateur dans la BD
        db.session.add(new_user)
        db.session.commit()

        # une fois inscrit, le nouvel utilisateur est redirigé sur la page de connexion
        return redirect(url_for('auth.login'))

    # affiche la page d'inscription pour un nouvel utilisateur
    return render_template('signup.html', title='Inscription')


@auth.route('/login', methods=['GET', 'POST'])
def login() -> str:
    ''' assure la connexion d'un utilisateur
    '''
    # si l'utilisateur clique sur le bouton de connexion
    if request.method == 'POST':
        # on récupère ses données renseignées via le formulaire
        email = request.form.get('email')
        password = request.form.get('password')

        # et on vérifie si l'utilisateur existe déjà
        user = User.query.filter_by(email=email).first()

        # si oui ou si ses identifiants sont incorrects après comparaison du mot de passe du formulaire à celui qui est inscrit dans la BD
        if not user or not check_password_hash(user.password, password):
            flash('Identifiants incorrects. Réessayez svp !')
            # il est amené à réessayer
            return redirect(url_for('auth.login'))

        # sinon tout se passe bien et il peut maintenant se connecter à la plateforme
        login_user(user, remember=True)
        return redirect(url_for('main.index'))

    # affichage de la page de connexion
    return render_template('login.html', title='Connexion')


@auth.route('/logout')
@login_required
def logout():
    ''' assure la déconnexion d'un utilisateur
    '''
    logout_user()  # déconnecte l'utilisateur
    # et le redirige sur la page de connexion
    return redirect(url_for('auth.login'))
