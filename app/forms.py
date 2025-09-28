from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField 
from wtforms.validators import DataRequired, Email

from app import db
from app.models import Contato

class ContatoForm(FlaskForm):
    nome = StringField('Nome',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired(),Email()])
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