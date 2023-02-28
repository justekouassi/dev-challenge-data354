from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    ''' représente un utilisateur
    '''
    # __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f'<Utilisateur N°{self.id} : {self.email}>'
