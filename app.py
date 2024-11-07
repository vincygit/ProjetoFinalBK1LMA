from flask import (Flask, flash, redirect, render_template, request, url_for) # importa o flask

app = Flask(__name__) # cria uma instância
app.secret_key = 'segredo'  # Para utilizar flash messages

@app.route('/')
def paginainicial():
    return render_template('index.html')

@app.route("/sobre", methods=('GET' ,))
def sobre():
    return render_template('sobre.html')