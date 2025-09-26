from app import app
from flask import render_template, url_for


@app.route('/')
def Homepage():
    usuario='Vítor'
    idade=34
    context={
        'usuario':usuario,
        'idade':idade
    }
    return render_template('index.html',context=context)


@app.route('/Contato/')
def nova():
    return render_template('nova.html')