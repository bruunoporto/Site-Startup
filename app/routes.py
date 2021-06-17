from flask_login.utils import login_required, logout_user
from werkzeug.security import generate_password_hash
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session
from app.model import usuario, empresa, Post, Event
from app.forms import LoginForm, RegisterEnterprise, RegisterUser, Comments, RegisterEvents
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.urls import url_parse
import datetime
##########################################################################


@app.route("/")
@app.route("/index")
def main_page():
    db.create_all()                              # PAGINA PRINCIPAL
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
                next_page = url_for('enterprise_page_specific',name=user.enterprise_name)
        return redirect(next_page)
    return render_template('login_page.html', title="Login", css_file="login_page.css", form=form,  user=current_user)
        #flash("Precisa inserir informação para user {}, lembra de mim = {}".format(form.username.data, form.remember_me.data))
        # redirect(url_for("main_page"))                             # PAGINA DE LOGIN
   
@app.route("/event_register_page", methods=["POST", "GET"])
@login_required
def event_register_page():
    form = RegisterEvents()
    if form.validate_on_submit():
        text = form.text.data
        name = form.name.data
        age_group = form.age_group.data
        interest = form.interest.data
        location = form.localization.data
        if location:
            latitude = form.latitude.data
            longitude = form.longitude.data
        else:
            latitude = current_user.latitude
            longitude = current_user.longitude
        date =  datetime.datetime.timestamp(datetime.datetime.combine(form.date.data, datetime.datetime.min.time()))
        id_max = 0
        for event in Event.query.all():
           if event.id > id_max:
            id_max = event.id+1
            try:
                if id_max == Event.query.filter_by(id = id_max).first().id:
                    id_max = id_max +1
                    print(id_max)
                else :
                    break
            except:
                break
        post = Event(id = id_max,body=text, timestamp = date, empresa_id=current_user.id,name = name, latitude=latitude,longitude = longitude, age_groups=age_group, event_type=interest)
        flash("Evento Salvo com Sucesso")
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('enterprise_page_specific',name=current_user.enterprise_name))
    return render_template('event_register_page.html', user=current_user, form = form, css_file="user_register_page.css", title="Eventos")

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
        latitude = form.latitude.data
        longitude = form.longitude.data
        pass_hash = generate_password_hash(senha)
        pessoa = empresa(id=id,enterprise_name=nome, password_hash=pass_hash,latitude= latitude,longitude=longitude, email = email, street=rua, district=bairro, city=cidade)
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

@app.route("/enterprise_page/<name>", methods=["POST", "GET"])
@login_required
def enterprise_page_specific(name):
    form = Comments()
    enterpriseS= empresa.query.filter_by(enterprise_name=name).first()
    if form.validate_on_submit():
        text = form.text.data
        id_max = 0
        for post in Post.query.all():
            if post.id >= id_max:
                id_max = post.id+1
        post = Post(id = id_max,body=text, timestamp = datetime.datetime.now().timestamp(), empresa_id=enterpriseS.id, author_id = current_user.id)
        flash("Post Salvo com Sucesso")
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('enterprise_page_specific',name=enterpriseS.enterprise_name))                        # PAGINA DE EMPRESA
    return render_template('enterprise_page.html', title=name, css_file="enterprise_page.css",user=current_user, usuario=usuario, enterprise=empresa, posts=Post.query.filter_by(empresa_id=enterpriseS.id), form=form, events=Event.query.filter_by(empresa_id=enterpriseS.id).all())
        
@app.route("/event_page/<name>", methods=["POST", "GET"])
@login_required
def event_page(name):
    form = Comments()
    eventoo = Event.query.filter_by(name=name).first()
    if form.validate_on_submit():
        return form.data
        text = form.text.data
        id_max = 0
        for post in Post.query.all():
            if post.id > id_max:
                id_max = post.id+1
        post = Post(id = id_max,body=text, timestamp = datetime.datetime.now().timestamp(), event_id=eventoo.id, author_id = current_user.id)
        flash("Post Salvo com Sucesso")
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('event_page',name=name))                        # PAGINA DE EMPRESA
    return render_template('event_page.html', title=name, css_file="event_page.css",user=current_user, usuario=usuario, enterprise=empresa, posts=Post.query.filter_by(event_id=eventoo.id), form=form, body=eventoo.body, id  =eventoo.empresa_id )    

@app.route("/user_page", methods=["POST", "GET"])
@login_required
def user_page():                              # PAGINA DE USUARIO
    return render_template('user_page.html', title="Usuario", eventos = Event ,css_file="user_page.css", user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main_page"))




