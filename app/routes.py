import flask_login
from flask_login.utils import login_required, logout_user
from app import app
from flask import render_template, request, redirect, url_for, flash
from app.model import usuario, empresa
from app.forms import LoginForm, RegisterEnterprise, RegisterUser
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.urls import url_parse
##########################################################################


@app.route("/")
@app.route("/index")
def main_page():                              # PAGINA PRINCIPAL
    return render_template('main_page.html', title="Home", css_file="main_page.css")


@app.route("/login_page", methods=["POST", "GET"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = usuario.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("senha incorreta")
            return redirect(url_for("login_page"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        #flash("Precisa inserir informação para user {}, lembra de mim = {}".format(form.username.data, form.remember_me.data))
        # redirect(url_for("main_page"))                             # PAGINA DE LOGIN
    return render_template('login_page.html', title="Login", css_file="login_page.css", form=form)


@app.route("/enterprise_register_page", methods=["POST", "GET"])
def enterprise_register_page():
    if request.method == "GET":
        form = RegisterEnterprise()               # PAGINA DE REGISTRO DE EMPRESA
        return render_template('enterprise_register_page.html', title="Seja um Anunciante", css_file="enterprise_register_page.css", form=form)
    elif request.method == "POST":
        nome = request.form["username"]
        senha = request.form["password"]
        tipo = request.form["tipo"]
        rua = request.form["rua"]
        cidade = request.form["cidade"]
        bairro = request.form["bairro"]
        numero = request.form["numero"]

        if nome == "" or senha == "":
            return "<h1>Por favor cadastre user e senha</h1>"
        else:
            pessoa = empresa(nome, senha, tipo, cidade, bairro, rua, numero)
            pessoa.registro_empresa()
            return "<h1>Registro salvo com sucesso</h1>"


@app.route("/user_register_page", methods=["POST", "GET"])
def user_register_page():
    if request.method == "GET":
        form = RegisterUser()                     # PAGINA DE REGISTRO DE USUARIO
        return render_template('user_register_page.html', title="Registro", css_file="user_register_page.css", form=form)
    elif request.method == "POST":
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


@app.route("/enterprise_page", methods=["POST", "GET"])
@login_required
def enterprise_page():                        # PAGINA DE EMPRESA
    return render_template('enterprise_page.html', title="Empresa", css_file="enterprise_page.css")


@app.route("/user_page", methods=["POST", "GET"])
@login_required
def user_page():                              # PAGINA DE USUARIO
    return render_template('user_page.html', title="Usuario", css_file="user_page.css")


@app.route("/comments_about_page", methods=["POST", "GET"])
def comments_about():                         # COMENTARIOS SOBRE MELHORIAS / FEEDBACKS
    return render_template('comments_about_page.html', title="Comentários")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))


app.run()
