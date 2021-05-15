from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    remember_me = BooleanField("Recordar registro")
    submit = SubmitField("Acessar")

class RegisterUser(FlaskForm):
    username = StringField("Nome", validators=[DataRequired()])
    age = StringField("Idade", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    city = StringField("Cidade", validators=[DataRequired()])
    district = StringField("Bairro", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Registrar")

class RegisterEnterprise(FlaskForm):
    username = StringField("Nome", validators=[DataRequired()])
    age = StringField("Idade", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    city = StringField("Cidade", validators=[DataRequired()])
    district = StringField("Bairro", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Registrar")

class RegisterEnterprise(FlaskForm):
    username = StringField("Nome Fantasia", validators=[DataRequired()])
    street = StringField("Rua", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    city = StringField("Cidade", validators=[DataRequired()])
    district = StringField("Bairro", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Registrar")