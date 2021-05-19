import sqlite3
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class usuario(UserMixin, db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    city = db.Column(db.String(120))
    district = db.Column(db.String(50))
    age = db.Column(db.Integer)

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class empresa(UserMixin, db.Model):
    __tablename__ = "empresa"
    id = db.Column(db.Integer,primary_key=True)
    enterprise_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    city = db.Column(db.String(120))
    latitude = db.Column(db.Float)
    logintude = db.Column(db.Float)
    district = db.Column(db.String(50))
    street = db.Column(db.String(120))

    def __repr__(self):
        return "<User {}>".format(self.enterprise_name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    if usuario.query.get(int(id)):
        load = usuario.query.get(int(id))
    else:
        load = empresa.query.get(int(id))
    return load


