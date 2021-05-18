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
    form = LoginForm()
    if form.validate_on_submit():
        user = usuario.query.filter_by(username=form.username.data).first()
        boole = True
        if user is None or not user.check_password(form.password.data):
            user = empresa.query.filter_by(enterprise_name=form.username.data).first()
            boole = False
            if user is None or not user.check_password(form.password.data):
                flash("Senha ou Usuario Incorretos")
                return redirect(url_for("login_page"))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            if  boole:
                next_page = url_for('user_page')
            else:
                next_page = url_for('enterprise_page')
        return redirect(next_page)
    return render_template('login_page.html', title="Login", css_file="login_page.css", form=form,  user=current_user)
        #flash("Precisa inserir informação para user {}, lembra de mim = {}".format(form.username.data, form.remember_me.data))
        # redirect(url_for("main_page"))                             # PAGINA DE LOGIN
   


@app.route("/enterprise_register_page", methods=["POST", "GET"])
def enterprise_register_page():
    
    form = RegisterEnterprise()               # PAGINA DE REGISTRO DE EMPRESA
    if form.validate_on_submit():
        id = form.document.data
        nome = form.username.data
        senha = form.password.data
        email = form.email.data
        rua = form.street.data
        cidade = form.city.data
        bairro = form.district.data
        pass_hash = generate_password_hash(senha)
        pessoa = empresa(id=id,enterprise_name=nome, password_hash=pass_hash, email = email, street=rua, district=bairro, city=cidade)
        flash("Regitro Salvo com Sucesso")
        db.session.add(pessoa)
        db.session.commit()
        return redirect(url_for("login_page"))
    return render_template('enterprise_register_page.html', title="Seja um Anunciante", css_file="enterprise_register_page.css", form=form,  user=current_user)
        
        


@app.route("/user_register_page", methods=["POST", "GET"])
def user_register_page():
    
    form = RegisterUser()                     # PAGINA DE REGISTRO DE USUARIO
    
    if form.validate_on_submit():
        id = form.document.data
        nome = form.username.data
        senha = form.password.data
        email = form.email.data
        idade= form.age.data    
        cidade = form.city.data
        bairro = form.district.data 
        pass_hash = generate_password_hash(senha)
        pessoa = usuario(id=id, username=nome, password_hash=pass_hash, email = email, age=idade, district=bairro, city=cidade)
        flash("Regitro Salvo com Sucesso")
        db.session.add(pessoa)
        db.session.commit()
        return redirect(url_for("login_page"))
    return render_template('user_register_page.html', title="Registro", css_file="user_register_page.css", form=form,  user=current_user)

@app.route("/enterprise_page", methods=["POST", "GET"])
@login_required
def enterprise_page():                        # PAGINA DE EMPRESA
    return render_template('enterprise_page.html', title="Empresa", css_file="enterprise_page.css",user=current_user, enterprise= current_user)

@app.route("/enterprise_page/<name>", methods=["POST", "GET"])
@login_required
def enterprise_page_specific(name):                        # PAGINA DE EMPRESA
    return render_template('enterprise_page.html', title=name, css_file="enterprise_page.css",user=current_user, enterprise=empresa.query.filter_by(enterprise_name=name).first())

@app.route("/user_page", methods=["POST", "GET"])
@login_required
def user_page():                              # PAGINA DE USUARIO
    return render_template('user_page.html', title="Usuario", empresa = empresa ,css_file="user_page.css", user=current_user)


@app.route("/comments_about_page", methods=["POST", "GET"])
def comments_about():                         # COMENTARIOS SOBRE MELHORIAS / FEEDBACKS
    return render_template('comments_about_page.html', title="Comentários",  user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main_page"))




app.run()
