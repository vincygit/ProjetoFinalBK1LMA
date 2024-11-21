from flask import (Flask, flash, redirect, render_template, request, url_for) # importa o flask
import json
import os

app = Flask(__name__) # cria uma instância
app.secret_key = 'segredo'  # Para utilizar flash messages

# Função para carregar os produtos do arquivo JSON
def carregar_produtos():
    if os.path.exists('produtos.json'):
        with open('produtos.json', 'r') as f:
            return json.load(f)
    return []

# Rota para a página inicial
@app.route('/')
def paginainicial():
    return render_template('index.html')


# Rota para a página de contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        # Salvar dados do contato em contatos.json
        novo_contato = {
            'nome': request.form['nome'],
            'email': request.form['email'],
            'mensagem': request.form['mensagem']
        }
        
        # Adiciona o novo contato ao arquivo contatos.json
        if os.path.exists('contatos.json'):
            with open('contatos.json', 'r+') as f:
                contatos = json.load(f)
                contatos.append(novo_contato)
                f.seek(0)
                json.dump(contatos, f, indent=2)
        else:
            with open('contatos.json', 'w') as f:
                json.dump([novo_contato], f, indent=2)

        return jsonify({"message": "Contato salvo com sucesso!"}), 200

    return render_template('contato.html')


# Rota para a página de produtos
@app.route('/produtos')
def produtos():
    produtos = carregar_produtos()
    return render_template('produtos.html', produtos=produtos)


#--------------------BLOG-----------------#

@app.route("/blog/dicas-para-manter-sua-bicicleta-em-perfeito-estado", methods=('GET' ,))
def dicas():
    return render_template('dicasbike.html')

@app.route("/blog/os-melhores-destinos-para-pedalar-no-brasil", methods=('GET' ,))
def destinos():
    return render_template('melhoresdestinos.html')

@app.route("/blog/como-escolher-a-bicicleta-certa-para-voce", methods=('GET' ,))
def escolherbike():
    return render_template('escolherbike.html')