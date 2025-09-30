from . import db, login_manager
from datetime import datetime, timezone 
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(100), nullable=True) 
    sobrenome = db.Column(db.String(100), nullable=True) 
    email = db.Column(db.String(150), nullable=True)
    senha = db.Column(db.String(150), nullable=True)
    posts = db.relationship('Post', backref='user', lazy=True)


class Contato(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    nome = db.Column(db.String(100), nullable=True) 
    email = db.Column(db.String(150), nullable=True)
    assunto = db.Column(db.String(100), nullable=True)
    mensagem = db.Column(db.Text, nullable=True)  
    respondido = db.Column(db.Integer, default=0)


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    mensagem = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def msg_resumo(self):
        return f'{self.mensagem[:10]}...'