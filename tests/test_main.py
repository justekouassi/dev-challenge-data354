import unittest
from flask_login import current_user
from backend import db, create_app
from backend.models import *
from .test_auth import TestAuth


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        ''' initialisation des tests de de visualisation
        '''
        TestAuth().setUp()

    def test_index(self) -> None:
        ''' test de la page de visualisation d'un utilisateur
        '''
        # connexion
        TestAuth().test_login()
        reponse = self.client.get('/', follow_redirects=True)
        self.assertEqual(reponse.status_code, 200)
        self.assertTrue(current_user.is_authenticated)
        self.assertIn('email@test.com', reponse.data)

    def tearDown(self) -> None:
        ''' nettoyage après les tests
        '''
        db.session.remove()
        db.drop_all()
