from . import app, db  
from flask import render_template, url_for, request
from .models import Contato 

@app.route('/')
def Homepage():
    usuario='Vítor'
    idade=34
    context={
        'usuario':usuario,
        'idade':idade
    }

    return render_template('index.html',context=context)

@app.route('/Contato/', methods=['GET', 'POST'])
def contato():
    context = {}
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        
        contato = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        db.session.add(contato)
        db.session.commit()

    return render_template('Contato_old.html', context=context)


# formato sem segurança(ou pouca)
@app.route('/Contato_old/', methods=['GET', 'POST'])
def Contato_old():

    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa': pesquisa})

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        
        contato = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        db.session.add(contato)
        db.session.commit()

    return render_template('Contato_old.html', context=context)