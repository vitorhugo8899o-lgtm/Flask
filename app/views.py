from . import app, db  
from flask import render_template, url_for, request, redirect 
from .models import Contato 
from app.forms import ContatoForm


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
    form = ContatoForm() 
    context = {} 
    
    if form.validate_on_submit():
        form.save() 
        
        return redirect(url_for('contato')) 
    
    return render_template('Contato.html', context=context, form=form) 


@app.route('/Contato_old/', methods=['GET', 'POST'])
def Contato_old():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa': pesquisa})
        
    return render_template('Contato.html', context=context)