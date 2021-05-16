from flask.globals import session
import flask_login
from random import randint
from flask_login.utils import login_required, logout_user
from werkzeug.security import generate_password_hash
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session
from app.model import usuario, empresa
from app.forms import LoginForm, RegisterEnterprise, RegisterUser
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.urls import url_parse
##########################################################################


@app.route("/")
@app.route("/index")
def main_page():                              # PAGINA PRINCIPAL
    return render_template('main_page.html', title="Home", css_file="main_page.css", user=current_user)


@app.route("/login_page", methods=["POST", "GET"])
def login_page():
    if request.method == "GET":
        form = LoginForm()
        return render_template('login_page.html', title="Login", css_file="login_page.css", form=form,  user=current_user)
    if request.method == "POST":
        user = usuario.query.filter_by(username=request.form["username"]).first()
        usuario == True
        if user is None or not user.check_password(request.form["password"]):
            user = empresa.query.filter_by(username=request.form["username"]).first()
            usuario == False
            if user is None or not user.check_password(request.form["password"]):
                flash("senha incorreta")
                return redirect(url_for("login_page"))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            if usuario:
                next_page = url_for('user_page')
            else:
                next_page = url_for('enterprise_page')
        return redirect(next_page)
        #flash("Precisa inserir informação para user {}, lembra de mim = {}".format(form.username.data, form.remember_me.data))
        # redirect(url_for("main_page"))                             # PAGINA DE LOGIN
   


@app.route("/enterprise_register_page", methods=["POST", "GET"])
def enterprise_register_page():
    if request.method == "GET":
        form = RegisterEnterprise()               # PAGINA DE REGISTRO DE EMPRESA
        return render_template('enterprise_register_page.html', title="Seja um Anunciante", css_file="enterprise_register_page.css", form=form,  user=current_user)
    elif request.method == "POST":
        id = randint(1,100000000000000000000000000000000000000000000000000000)
        nome = request.form["username"]
        senha = request.form["password"]
        email = request.form["email"]
        rua = request.form["street"]
        cidade = request.form["city"]
        bairro = request.form["district"]
        pass_hash = generate_password_hash(senha)
        pessoa = empresa(id=id,enterprise_name=nome, password_hash=pass_hash, email = email, street=rua, district=bairro, city=cidade)
        flash("Regitro Salvo com Sucesso")
        db.session.add(pessoa)
        db.session.commit()
        return redirect(url_for("login_page"))
        
        


@app.route("/user_register_page", methods=["POST", "GET"])
def user_register_page():
    if request.method == "GET":
        form = RegisterUser()                     # PAGINA DE REGISTRO DE USUARIO
        return render_template('user_register_page.html', title="Registro", css_file="user_register_page.css", form=form,  user=current_user)
    elif request.method == "POST":
        id = randint(1,1000000000000000000000000000000000000000)
        nome = request.form["username"]
        senha = request.form["password"]
        email = request.form["email"]
        idade= request.form["age"]
        cidade = request.form["city"]
        bairro = request.form["district"]
        pass_hash = generate_password_hash(senha)
        pessoa = usuario(id=id, username=nome, password_hash=pass_hash, email = email, age=idade, district=bairro, city=cidade)
        flash("Regitro Salvo com Sucesso")
        db.session.add(pessoa)
        db.session.commit()
        return redirect(url_for("login_page"))


@app.route("/enterprise_page", methods=["POST", "GET"])
@login_required
def enterprise_page():                        # PAGINA DE EMPRESA
    return render_template('enterprise_page.html', title="Empresa", css_file="enterprise_page.css",user=current_user)


@app.route("/user_page", methods=["POST", "GET"])
@login_required
def user_page():                              # PAGINA DE USUARIO
    return render_template('user_page.html', title="Usuario", css_file="user_page.css", user=current_user)


@app.route("/comments_about_page", methods=["POST", "GET"])
def comments_about():                         # COMENTARIOS SOBRE MELHORIAS / FEEDBACKS
    return render_template('comments_about_page.html', title="Comentários",  user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main_page"))


app.run()
