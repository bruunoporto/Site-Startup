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

    def registro_usuario(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES ('"+self.__nome+"','"+self.__idade+"','" +
                    self.__senha+"','"+self.__cidade+"','"+self.__bairro+"','"+self.__documento+"')")
        con.commit()
        con.close()


class empresa(db.Model):
    __tablename__ = "empresa"
    id = db.Column(db.Integer,primary_key=True)
    enterprise_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    city = db.Column(db.String(120))
    district = db.Column(db.String(50))
    street = db.Column(db.String(120))

    def __repr__(self):
        return "<User {}>".format(self.enterprise_name)

    # def __init__(self, nome_empresa, senha , tipo_empresa, cidade_empresa, bairro_empresa, rua_empresa, numero_empresa):
    #    self.__nome_empresa = nome_empresa
    #    self.__tipo_empresa = tipo_empresa
    #    self.__senha = senha
    #    self.__cidade_empresa = cidade_empresa
    #    self.__bairro_empresa = bairro_empresa
    #    self.__rua_empresa = rua_empresa
    #    self.__numero_empresa = numero_empresa
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def registro_empresa(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("INSERT INTO enterprises VALUES ('"+self.__nome_empresa+"','"+self.__tipo_empresa+"','"+self.__senha +
                    "','"+self.__cidade_empresa+"','"+self.__bairro_empresa+"','"+self.__rua_empresa+"','"+self.__numero_empresa+"')")
        con.commit()
        con.close()


def login_model(nome, senha):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    for el in cur.execute("SELECT * FROM users"):
        if el[0] == nome:
            if el[2] == senha:
                con.commit()
                con.close()
                return (True, "Usuario")
    for el in cur.execute("SELECT * FROM enterprises"):
        if el[0] == nome:
            print("opa")
            if el[2] == senha:
                con.commit()
                con.close()
                return (True, "Empresa")
    con.commit()
    con.close()
    return (False, "")


@login.user_loader
def load_user(id):
    return usuario.query.get(int(id))

#con = sqlite3.connect('database.db')
#cur = con.cursor()

# Create table
# cur.execute('''CREATE TABLE enterprises (name text, type text, password text, city text, neighborhood text, street text, number real)''')
# cur.execute('''CREATE TABLE users (name text, age real, password text, city text, neighborhood text, document real)''')

# Insert a row of data
# cur.execute("INSERT INTO users VALUES ('Pedro Henrique',18,'12345678','Rio de Janeiro','Leblon','17120554700')")
# cur.execute("INSERT INTO enterprises VALUES ('Beco dos fodao','Boca de fumo','12345678','Rio de Janeiro','Leblon','Rua Professor Saboia Ribeiro',83)")
# Save (commit) the changes
# con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
# con.close()
