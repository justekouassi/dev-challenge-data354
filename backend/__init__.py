from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# initialisation de SQLAlchemy
db = SQLAlchemy()


def create_app() -> Flask:
    ''' fonction principale qui génère l'application
    '''
    app = Flask(__name__)

    # configuration de l'application
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

	# initialisation de l'application Flask
    db.init_app(app)

	# configuration du système d'authentification pour l'application
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint pour les routes d'authentification (accessibles à tous)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint pour les routes de visualisation (sécurisées et accessibles aux utilisateurs connectés)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
