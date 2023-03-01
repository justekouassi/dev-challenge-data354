import unittest
from flask_login import current_user
from backend import db, create_app
from backend.models import *


class TestAuth(unittest.TestCase):

    def setUp(self) -> None:
        ''' initialisation des tests d'authentification
        '''
        # initialisation de l'application
        app = create_app()
        # configuration de l'application pour les tests
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
        # création de la DB de test
        with app.app_context():
            db.create_all()
        # création d'un email de test
        user = User(email='email@test.com', password='supersecret')
        db.session.add(user)
        db.session.commit()
        # création d'un test client por l'application
        self.client = app.test_client()

    def test_signup(self) -> None:
        ''' test d'inscription d'un utilisateur
        '''
        # on se connecte à la plateforme
        reponse = self.client.post('/signup', data=dict(
            email='email@signup.test',
            password='supersecret'
        ), follow_redirects=True)
        # le client est censé accéder correctement à la page de connexion
        self.assertEqual(reponse.status_code, 200)

    def test_login(self) -> None:
        ''' test de connexion d'un utilisateur
        '''
        # on se connecte à la plateforme
        reponse = self.client.post('/login', data=dict(
            email='email@test.com',
            password='supersecret'
        ), follow_redirects=True)
        # l'on est censé accéder correctement à la page de visualisation
        self.assertEqual(reponse.status_code, 200)
        # en étant authentifié
        self.assertTrue(current_user.is_authenticated)

    def test_logout(self) -> None:
        ''' test de déconnexion d'un utilisateur
        '''
        # on se connecte d'abord à la plateforme
        # normal la déconnexion vient après la connexion :)
        self.test_login()

        # déconnexion de l'utilisateur
        reponse = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(reponse.status_code, 200)
        self.assertFalse(current_user.is_authenticated)
        self.assertIn(b'Connexion', reponse.data)

    def tearDown(self) -> None:
        ''' nettoyage après les tests d'authentification
        '''
        db.session.remove()
        db.drop_all()
