from . import app, db  
from flask import render_template, url_for, request, redirect 
from .models import Contato 
from app.forms import ContatoForm, UserForm
from flask_login import login_user, logout_user, current_user


@app.route('/')
def Homepage():
    usuario='Vítor'
    idade=34
    context={
        'usuario':usuario,
        'idade':idade
    }

    return render_template('index.html',context=context)


@app.route('/Cadastro/', methods=['GET', 'POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        user = form.Save()
        login_user(user, remember=True)
        return redirect(url_for('Homepage'))
    return render_template('Cadastro.html',form=form)


@app.route('/Contato/', methods=['GET', 'POST'])
def contato():
    form = ContatoForm() 
    context = {} 
    
    if form.validate_on_submit():
        form.save() 
        
        return redirect(url_for('contato')) 
    
    return render_template('Contato.html', context=context, form=form) 


@app.route('/Contato/Lista',)
def contatoLista():
    dados = Contato.query.order_by('nome')

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa','')

    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)


    context = {'dados':dados.all()}
    return render_template('Contato_Lista.html', context=context)

@app.route('/Contato/<int:id>/')

def contatoDetail(id):
    obj = Contato.query.get(id)

    return render_template('contato_detail.html', obj=obj)


@app.route('/Contato_old/', methods=['GET', 'POST'])
def Contato_old():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa': pesquisa})
        
    return render_template('Contato.html', context=context)