from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired("Insira seu Nome")])
    password = PasswordField("Senha", validators=[DataRequired("Insira sua senha")])
    remember_me = BooleanField("Recordar registro")
    submit = SubmitField("Acessar")

class RegisterUser(FlaskForm):
    username = StringField("Nome", validators=[DataRequired("Insira seu Nome")])
    age = StringField("Idade", validators=[DataRequired("Insira sua Idade")])
    document = StringField("CPF", validators=[DataRequired("Insira seu CPF")])
    email = StringField("Email", validators=[DataRequired("Insira seu email"),Email("Seu email está incorreto")])
    city = StringField("Cidade", validators=[DataRequired("Insira sua cidade")])
    district = StringField("Bairro", validators=[DataRequired("Insira seu Bairro")])
    password = PasswordField("Senha", validators=[DataRequired("Insira sua senha")])
    password_confirmation = PasswordField("Repita sua Senha", validators=[DataRequired("Insira sua senha"),EqualTo('password', message="As duas senhas devem ser iguais")])
    submit = SubmitField("Registrar")
class RegisterEnterprise(FlaskForm):
    username = StringField("Nome Fantasia", validators=[DataRequired("Insira seu Nome")])
    document = StringField("CNPJ", validators=[DataRequired("Insira seu CNPJ")])
    street = StringField("Rua", validators=[DataRequired("Insira sua rua")])
    email = StringField("Email", validators=[DataRequired("Insira seu email"),Email("Seu email está incorreto")])
    city = StringField("Cidade", validators=[DataRequired("Insira sua cidade")])
    district = StringField("Bairro", validators=[DataRequired("Insira seu Bairro")])
    password = PasswordField("Senha", validators=[DataRequired("Insira sua senha")])
    password_confirmation = PasswordField("Repita sua Senha", validators=[DataRequired("Insira novamente sua senha"), EqualTo('password', message="As duas senhas devem ser iguais")])
    submit = SubmitField("Registrar")