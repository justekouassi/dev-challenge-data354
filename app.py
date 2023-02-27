''' Point d'entrée de l'application
'''

from flask import Flask, render_template, jsonify
# import MySQLdb.cursors
# from flask_mysqldb import MySQL
import re
from graphique import generate_plot

app = Flask(__name__)
app.secret_key = 'justix'

# connexion à la base de données
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'data354'

# Intialisation de MySQL
# mysql = MySQL(app)


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


# @app.route('/login', methods=['GET', 'POST'])
# def login() -> str:
#     ''' assure la connexion d'un utilisateur
#     '''
#     # Output message if something goes wrong...
#     msg = ''
#     # vérifie si l'utilisateur a bien rempli le formulaire
#     if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
#         # création des variables
#         email = request.form['email']
#         password = request.form['password']
#     # vérifie si le compte existe
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute(
#         'SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
#     # Fetch one record and return result
#     user = cursor.fetchone()
#     # If user exists in users table in out database
#     if user:
#         # Create session data, we can access this data in other routes
#         session['loggedin'] = True
#         session['id'] = user['id']
#         session['username'] = user['username']
#         # Redirect to home page
#         return 'Logged in successfully!'
#     else:
#         # user doesnt exist or username/password incorrect
#         msg = 'Incorrect username/password!'
#     return render_template('login.html', msg='', title='Connexion')


@app.route('/signup')
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
