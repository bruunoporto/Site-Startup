from flask import Flask
from flask import render_template, request
from database import usuario, empresa

##########################################################################

app = Flask(__name__)


@app.route("/")
def main_page():                              # PAGINA PRINCIPAL
    return render_template('main_page.html')


@app.route("/login_page", methods = ["POST", "GET"])
def login_page():                             # PAGINA DE LOGIN
    return render_template('login_page.html')


@app.route("/enterprise_register_page", methods = ["POST", "GET"])
def entreprise_register_page():               # PAGINA DE REGISTRO DE EMPRESA
    return render_template('enterprise_register_page.html')


@app.route("/user_register_page", methods = ["POST", "GET"])
def user_register_page():                     # PAGINA DE REGISTRO DE USUARIO
    return render_template('user_register_page.html')


@app.route("/enterprise_page", methods = ["POST", "GET"])
def enterprise_page():                        # PAGINA DE EMPRESA
    return render_template('enterprise_page.html')


@app.route("/user_page", methods = ["POST", "GET"])
def user_page():                              # PAGINA DE USUARIO
    return render_template('user_page.html')


@app.route("/comments_about_page", methods = ["POST", "GET"])
def comments_about():                         # COMENTARIOS SOBRE MELHORIAS / FEEDBACKS
    return render_template('comments_about_page.html')

app.run()
