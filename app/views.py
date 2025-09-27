from app import app
from flask import render_template, url_for, request


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
def nova():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa': pesquisa})
    if request.method == 'POST':
        pesquisa = request.form['pesquisa']
        print('POST',pesquisa)
    return render_template('Contato.html', context=context)