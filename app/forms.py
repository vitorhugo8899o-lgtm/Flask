from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField 
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import db, bcrypt
from app.models import Contato, User

class UserForm(FlaskForm):
    nome = StringField('Nome',validators=[DataRequired()])
    sobrenome = StringField('Sobrenome',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired(), Email()])
    senha = PasswordField('Senha',validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirmação de Senha',validators=[DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

    def validade_email(self,email):
        if User.query.filter(email=email.data).first():
            return ValidationError('Usuário já cadastrado com esse E-mail!!')

    def Save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        user = User(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha
        )

        db.session.add(user)
        db.session.commit()
        return user
    

class LoginForm(FlaskForm):
    email = StringField('E-mail',validators=[DataRequired(), Email()])
    senha = PasswordField('Senha',validators=[DataRequired()])
    btnSubmit = SubmitField('Cadastrar')

    def login(self):
        user = User.query.filter_by(email=self.email.data).first()

        if user:
            if bcrypt.check_password_hash(user.senha,self.senha.data.encode('utf-8') ):
                return user
            else:
                raise Exception('Senha incorreta')

        else:
            raise Exception('Usuário não encontrado')


class ContatoForm(FlaskForm):
    nome = StringField('Nome',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired(), Email()])
    assunto = StringField('Assunto',validators=[DataRequired()])
    mensagem = TextAreaField('Mensagem',validators=[DataRequired()]) 
    btnSubmit = SubmitField('Enviar')

    def save(self):
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
            )
        db.session.add(contato)
        db.session.commit()