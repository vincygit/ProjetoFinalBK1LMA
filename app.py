from flask import (Flask, flash, redirect, render_template, request, url_for) # importa o flask
import json
import os

app = Flask(__name__) # cria uma instância
app.secret_key = 'segredo'  # Para utilizar flash messages


class CRUD:
    caminho = "produtos.json" # é possível usar crud.caminho = 'novo.json'
    def __init__(self, modo) -> None:
        self.modo = modo

    def set_nome(self, nome):
        set.nome = nome

    def conexao(self, dados=None):
        """
            modo: '+r' para leitura
            modo: '+w' para escrita
        """
        with open(self.caminho, self.modo, encoding='utf8') as file:
            if self.modo == '+w':
                file.write(dados)
            elif self.modo == '+r':
                return file.read()


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

# Rota para a página sobre
@app.route("/sobre", methods=('GET' ,))
def sobre():
    return render_template('sobre.html')


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

#--------------------BLOG-----------------#

@app.route("/blog/confira-12-dicas-para-manter-a-sua-bicicleta-sempre-em-dia", methods=('GET' ,))
def dicas():
    return render_template('dicasbike.html')

@app.route("/blog/melhores-destinos-brasil-mountain-bike", methods=('GET' ,))
def destinos():
    return render_template('melhoresdestinos.html')

@app.route("/blog/como-escolher-a-bike-perfeita-para-voce", methods=('GET' ,))
def escolherbike():
    return render_template('escolherbike.html')



#--------------------PRODUTOS-----------------#
#@app.route('/produtos/<int:id>')
#def produto(id):
    produtos = carregar_produtos()
    produto_encontrado = next((produto for produto in produtos if produto['id'] == id), None)
    
    if produto_encontrado:
        return render_template('produtos.html', produto=produto_encontrado)
    else:
        flash('Produto não encontrado!')
        return redirect(url_for('produtos'))
    

@app.route('/produtos')
def produtos():
    produtos = carregar_produtos()
    return render_template('produtos.html', produtos=produtos)