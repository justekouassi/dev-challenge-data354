import unittest
from flask_login import current_user
from backend import db, create_app
from backend.models import *


class TestLogout(unittest.TestCase):

    def setUp(self) -> None:
        ''' initialisation des tests de déconnexion
        '''
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
        with app.app_context():
            db.create_all()
        user = User(email='email@test.com', password='supersecret')
        db.session.add(user)
        db.session.commit()
        self.client = app.test_client()

    def test_logout(self) -> None:
        ''' test de déconnexion d'un utilisateur
        '''
        # on se connecte d'abord à la plateforme
        # normal la déconnexion vient après la connexion :)
        reponse = self.client.post('/login', data=dict(
            email='email@test.com',
            password='supersecret'
        ), follow_redirects=True)
        self.assertEqual(reponse.status_code, 200)
        self.assertTrue(current_user.is_authenticated)

        # déconnexion de l'utilisateur
        reponse = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(reponse.status_code, 200)
        self.assertFalse(current_user.is_authenticated)
        self.assertIn(b'Connexion', reponse.data)

    def tearDown(self) -> None:
        ''' nettoyage après les tests
        '''
        db.session.remove()
        db.drop_all()
