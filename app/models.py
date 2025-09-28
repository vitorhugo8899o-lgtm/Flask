from . import db
from datetime import datetime, timezone 

class Contato(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    nome = db.Column(db.String(100), nullable=True) 
    email = db.Column(db.String(150), nullable=True)
    assunto = db.Column(db.String(100), nullable=True)
    mensagem = db.Column(db.Text, nullable=True)  
    respondido = db.Column(db.Integer, default=0)