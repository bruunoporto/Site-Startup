from flask import Flask
from flask import render_template, request

app = Flask(__name__)  # CRIA O OBJETO


@app.route("/")  # CRIA A ROTA
def main_page():                              # PAGINA PRINCIPAL
    pass

@app.route("/enterprise_register_page", methods = ["POST", "GET"])
def entreprise_register_page():               # PAGINA DE REGISTRO DE EMPRESA
    pass

@app.route("/user_register_page", methods = ["POST", "GET"])
def user_register_page():                     # PAGINA DE REGISTRO DE USUARIO
    pass

@app.route("/login_page", methods = ["POST", "GET"])
def login_page():                             # PAGINA DE LOGIN
    pass

@app.route("/enterprise_page", methods = ["POST", "GET"])
def enterprise_page():                        # PAGINA DE EMPRESA
    pass

@app.route("/user_page", methods = ["POST", "GET"])
def user_page():                              # PAGINA DE USUARIO
    pass

@app.route("/comments_about_page", methods = ["POST", "GET"])
def comments_about():                         # COMENTARIOS SOBRE MELHORIAS / FEEDBACKS
    pass