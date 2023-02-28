import unittest
from flask import session, url_for
from flask_login import current_user
from backend import create_app, db

class TestAuth(unittest.TestCase):
    ''' cette classe permet de tester les fonctions d'authentification
    '''

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        cursor = mc.connection.cursor()
        cursor.execute('DELETE FROM users WHERE username = %s', ('test_user',))
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', ('test_user', hashlib.sha256('test_password'.encode()).hexdigest()))
        mc.connection.commit()

    def tearDown(self):
        cursor = mc.connection.cursor()
        cursor.execute('DELETE FROM users WHERE username = %s', ('test_user',))
        mc.connection.commit()
        self.app_context.pop()

    def test_login_valid_credentials(self):
        response = self.client.post('/login', data={'username': 'test_user', 'password': 'test_password'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(session['user_id'], '1')

    def test_login_invalid_credentials(self):
        response = self.client.post('/login', data={'username': 'test_user', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('user_id', session)
        self.assertIn(b'Invalid username or password', response.data)

    def test_login_missing_fields(self):
        response = self.client.post('/login', data={'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('user_id', session)
        self.assertIn(b'This field is required.', response.data)

    def test_logout(self):
        with self.client.session_transaction() as sess:
            sess['user_id'] = '1'
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('user_id', session)

    def test_index_authenticated(self):
        with self.client.session_transaction() as sess:
            sess['user_id'] = '1'
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, test_user', response.data)

    def test_index_not_authenticated(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.location)