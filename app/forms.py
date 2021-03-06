from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, HiddenField
from wtforms.fields.html5 import DateField
from wtforms.fields.simple import FileField
from wtforms.validators import DataRequired, EqualTo, Email,  ValidationError

def IntegerCheck(form, field):
    try:
        float(field.data)
    except:
        if field.data == "":
            return 0
        if str(field.label)[12:20] == "latitude" or str(field.label)[12:21] == "longitude":
            raise ValidationError('O dado deve ser um número, utilizando ponto como separador da parte inteira para a decimal')
        else:
            raise ValidationError("O dado deve ser um número")
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired("Insira seu Nome")])
    password = PasswordField("Senha", validators=[DataRequired("Insira sua senha")])
    remember_me = BooleanField("Recordar registro")
    submit = SubmitField("Acessar")

class RegisterUser(FlaskForm):
    username = StringField("Nome", validators=[DataRequired("Insira seu Nome")])
    age = StringField("Idade", validators=[DataRequired("Insira sua Idade"), IntegerCheck])
    document = StringField("CPF", validators=[DataRequired("Insira seu CPF"),IntegerCheck])
    email = StringField("Email", validators=[DataRequired("Insira seu email"),Email("Seu email está incorreto")])
    city = StringField("Cidade", validators=[DataRequired("Insira sua cidade")])
    district = StringField("Bairro", validators=[DataRequired("Insira seu Bairro")])
    password = PasswordField("Senha", validators=[DataRequired("Insira sua senha")])
    password_confirmation = PasswordField("Repita sua Senha", validators=[DataRequired("Insira sua senha"),EqualTo('password', message="As duas senhas devem ser iguais")])
    submit = SubmitField("Registrar")
    
class RegisterEnterprise(FlaskForm):
    username = StringField("Nome Fantasia", validators=[DataRequired("Insira seu Nome")])
    document = StringField("CNPJ", validators=[DataRequired("Insira seu CNPJ"),IntegerCheck])
    street = StringField("Rua", validators=[DataRequired("Insira sua rua")])
    email = StringField("Email", validators=[DataRequired("Insira seu email"),Email("Seu email está incorreto")])
    city = StringField("Cidade", validators=[DataRequired("Insira sua cidade")])
    district = StringField("Bairro", validators=[DataRequired("Insira seu Bairro")])
    password = PasswordField("Senha", validators=[DataRequired("Insira sua senha")])
    latitude = StringField("Latitude da sua localização", validators=[DataRequired("Insira sua Latitude"),IntegerCheck])
    longitude = StringField("Longitude da sua localização", validators=[DataRequired("Insira sua Longitude"),IntegerCheck])
    password_confirmation = PasswordField("Repita sua Senha", validators=[DataRequired("Insira novamente sua senha"), EqualTo('password', message="As duas senhas devem ser iguais")])
    submit = SubmitField("Registrar")
    
class Comments(FlaskForm):
    files = FileField("De upload em sua foto")
    evaluation = TextAreaField("",validators=[DataRequired("Dê sua avaliação")])
    text = TextAreaField("Escreva seu Comentário", validators=[DataRequired("Escreva seu comentário!")]) 
    submit = SubmitField("Registrar")

class RegisterEvents(FlaskForm):
    name = StringField("Escreva o nome do seu evento", validators=[DataRequired("Insira o nome do evento")])
    text = TextAreaField("Escreva a descrição do evento")#, validators=[DataRequired("Escreva seu comentário!")]) 
    age_group =SelectField("Faixa Etária :", choices=[('18-23', '18-23'), ('23-32', '23-32'), ('32-44', '32-44'), ('44-60', '44-60'), ('60+','60+'),('todos','Todas as Idades')],validators=[DataRequired("Insira a Faixa Etária")])
    localization = BooleanField("O evento é em uma localização diferente da da minha empresa")
    interest = SelectField("Tipo do Evento :", choices=[('animado', 'Animado'), ('calmo', 'Calmo'), ('ambos', 'Ambos')],validators=[DataRequired("Insira o tipo do evento")])
    date = DateField("Data do evento :",validators=[DataRequired("Insira a data do evento")])
    latitude = StringField("Latitude da sua localização", validators=[IntegerCheck])
    longitude = StringField("Longitude da sua localização", validators=[IntegerCheck])
    submit = SubmitField("Registrar")