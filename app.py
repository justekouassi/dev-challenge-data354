''' Point d'entrée de l'application
'''

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from graphique import generate_plot

app = Flask(__name__)
app.secret_key = 'justix'

# connexion à la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///project.db'

# Intialisation de SQLAlchemy
db = SQLAlchemy()
db.init_app(app)


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


@app.route('/')
def index() -> str:
    ''' représente la page principale de notre application
    qui affiche la visualisation des données prises l'un des
    capteurs en fonction d'une période donnée
    '''
    graphJSON = generate_plot()
    return render_template('index.html', title='Accueil', graphJSON=graphJSON)


@app.route('/graph')
def graph():
    graphJSON = generate_plot()
    return graphJSON


@app.route('/login', methods=['GET', 'POST'])
def login() -> str:
    ''' assure la connexion d'un utilisateur
    '''
    return render_template('login.html', title='Connexion')


@app.route('/signup', methods=['POST'])
def signup() -> str:
    ''' assure l'inscription d'un utilisateur
    '''
    return render_template('signup.html', title='Inscription')


@app.route('/prediction')
def prediction() -> str:
    ''' assure la prédiction
    '''
    return render_template('prediction.html', title='Prédiction')


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='127.0.0.1', port='4000', debug=True)
