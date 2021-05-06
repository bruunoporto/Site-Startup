from flask import Flask
from flask import render_template, request, redirect
from model import usuario, empresa, login_model

##########################################################################

app = Flask(__name__)


@app.route("/")
def main_page():                              # PAGINA PRINCIPAL
    return render_template('main_page.html')


@app.route("/login_page", methods = ["POST", "GET"])
def login_page():                             # PAGINA DE LOGIN
    return render_template('login_page.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    
    if request.method  == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        log = login_model(nome,senha)
        if not log[0]:
            return "<h1>Por favor cadastre user e senha</h1>"
        else:
            if log[1] == "Empresa":
                return redirect("/enterprise_page")
            elif log[1] == "Usuario":
                return redirect("/user_page")

@app.route("/enterprise_register_page", methods = ["POST", "GET"])
def entreprise_register_page():               # PAGINA DE REGISTRO DE EMPRESA
    return render_template('enterprise_register_page.html')


@app.route("/user_register_page", methods = ["POST", "GET"])
def user_register_page():                     # PAGINA DE REGISTRO DE USUARIO
    return render_template('user_register_page.html')

@app.route("/user_register", methods = ["POST", "GET"])
def cadastro():
    
    if request.method  == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        idade = request.form["idade"]
        documento = request.form["cpf"]
        cidade = request.form["cidade"]
        bairro = request.form["bairro"]
        
        if nome == "" or senha == "":
            return "<h1>Por favor cadastre user e senha</h1>"
        else:
            pessoa = usuario(senha, nome, idade, documento, cidade, bairro)
            pessoa.registro_usuario()
            return "<h1>Registro salvo com sucesso</h1>"
    
@app.route("/enterprise_page", methods = ["POST", "GET"])
def enterprise_page():                        # PAGINA DE EMPRESA
    return render_template('enterprise_page.html')

@app.route("/enterprise_register", methods = ["POST", "GET"])
def cadastro_empresa():

    if request.method  == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        tipo = request.form["tipo"]
        rua = request.form["rua"]
        cidade = request.form["cidade"]
        bairro = request.form["bairro"]
        numero = request.form["numero"]

        if nome == "" or senha == "":
            return "<h1>Por favor cadastre user e senha</h1>"
        else:
            pessoa = empresa(nome, senha , tipo, cidade, bairro, rua, numero)
            pessoa.registro_empresa()
            return "<h1>Registro salvo com sucesso</h1>"

@app.route("/user_page", methods = ["POST", "GET"])
def user_page():                              # PAGINA DE USUARIO
    return render_template('user_page.html')


@app.route("/comments_about_page", methods = ["POST", "GET"])
def comments_about():                         # COMENTARIOS SOBRE MELHORIAS / FEEDBACKS
    return render_template('comments_about_page.html')

app.run()
