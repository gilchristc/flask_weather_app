from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column('idUsers', db.Integer, primary_key=True)
    username = db.Column('username', db.String(64), index=True, unique=True)
    password_hash = db.Column('password_hash', db.String(128))
    email = db.Column('email', db.String(120), index=True, unique=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))