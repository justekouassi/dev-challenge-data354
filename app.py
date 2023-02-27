''' Point d'entrée de l'application
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    ''' représente la page principale de notre application 
    qui affiche la visualisation des données prises l'un des
    capteurs en fonction d'une période donnée
    '''
    return render_template("index.html", title="Accueil")


@app.route('/login')
def login() -> str:
    ''' assure la connexion d'un utilisateur
    '''
    return render_template("login.html", title="Connexion")


@app.route('/signup')
def signup() -> str:
    ''' assure l'inscription d'un utilisateur
    '''
    return render_template("signup.html", title="Inscription")


@app.route('/prediction')
def prediction() -> str:
    ''' assure la prédiction
    '''
    return render_template("prediction.html", title="Prédiction")


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='127.0.0.1', port='4000', debug=True)
