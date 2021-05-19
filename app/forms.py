from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email,  StopValidation

def IntegerCheck(form, field):
    try:
        float(field.data)
    except:
        StopValidation('O dado deve ser um número')
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired("Insira seu Nome")])
    password = PasswordField("Senha", validators=[DataRequired("Insira sua senha")])
    remember_me = BooleanField("Recordar registro")
    submit = SubmitField("Acessar")

class RegisterUser(FlaskForm):
    username = StringField("Nome", validators=[DataRequired("Insira seu Nome")])
    age = IntegerField("Idade", validators=[DataRequired("Insira sua Idade corretamente"), IntegerCheck])
    document = IntegerField("CPF", validators=[DataRequired("Insira seu CPF corretamente"),IntegerCheck])
    email = StringField("Email", validators=[DataRequired("Insira seu email"),Email("Seu email está incorreto")])
    city = StringField("Cidade", validators=[DataRequired("Insira sua cidade")])
    district = StringField("Bairro", validators=[DataRequired("Insira seu Bairro")])
    password = PasswordField("Senha", validators=[DataRequired("Insira sua senha")])
    password_confirmation = PasswordField("Repita sua Senha", validators=[DataRequired("Insira sua senha"),EqualTo('password', message="As duas senhas devem ser iguais")])
    submit = SubmitField("Registrar")
class RegisterEnterprise(FlaskForm):
    username = StringField("Nome Fantasia", validators=[DataRequired("Insira seu Nome")])
    document = IntegerField("CNPJ", validators=[DataRequired("Insira seu CNPJ corretamente"),IntegerCheck])
    street = StringField("Rua", validators=[DataRequired("Insira sua rua")])
    email = StringField("Email", validators=[DataRequired("Insira seu email"),Email("Seu email está incorreto")])
    city = StringField("Cidade", validators=[DataRequired("Insira sua cidade")])
    district = StringField("Bairro", validators=[DataRequired("Insira seu Bairro")])
    password = PasswordField("Senha", validators=[DataRequired("Insira sua senha")])
    latitude = IntegerField("Latitude da sua localização", validators=[DataRequired("Insira sua Latitude corretamente, utilizando ponto como separador da parte inteira para a decimal"),IntegerCheck])
    logitude = IntegerField("Longitude da sua localização", validators=[DataRequired("Insira sua Longitude corretamente,  utilizando ponto como separador da parte inteira para a decimal"),IntegerCheck])
    password_confirmation = PasswordField("Repita sua Senha", validators=[DataRequired("Insira novamente sua senha"), EqualTo('password', message="As duas senhas devem ser iguais")])
    submit = SubmitField("Registrar")