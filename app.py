from flask import (Flask, flash, redirect, render_template, request, url_for) # importa o flask
import json
import os

app = Flask(__name__) # cria uma instância
app.secret_key = 'segredo'  # Para utilizar flash messages


CONTATOS_FILE = "contatos.json"
PRODUTOS_FILE = "produtos.json"

def save_contato_to_file(data):
    if os.path.exists(CONTATOS_FILE):
        with open(CONTATOS_FILE, "r") as file:
            contatos = json.load(file)
    else:
        contatos = []

    contatos.append(data)

    with open(CONTATOS_FILE, "w") as file:
        json.dump(contatos, file, indent=4)

def save_compra_to_file(data):
    if os.path.exists(PRODUTOS_FILE):
        with open(PRODUTOS_FILE, "r") as file:
            try:
                compras = json.load(file)
            except json.JSONDecodeError:
                contatos = []  # Inicializa como uma lista vazia se houver erro
    else:
        compras = []

    compras.append(data)

    with open(PRODUTOS_FILE, "w") as file:
        json.dump(compras, file, indent=4)

lista_produtos = [
    {"id": 1, "nome": "Bicicleta aro 29 KRW", "preco": 792.30, "imagem": "bike1.webp"},
    {"id": 2, "nome": "Bicicleta aro 29 Dropp Z3", "preco": 787.55, "imagem": "bike2.webp"},
    {"id": 3, "nome": "Bicicleta Aro 29 Gts", "preco": 835.05, "imagem": "bike3.webp"},
    {"id": 4, "nome": "Bicicleta Aro 29 Aço Carbono Ksvj", "preco": 704.90, "imagem": "bike4.webp"},
    {"id": 5, "nome": "Bicicleta 29 GTS M1", "preco": 1606.11, "imagem": "bike5.webp"},
    {"id": 6, "nome": "Bicicleta Aro 29 KRW Alumínio Shimano TZ", "preco": 849.30, "imagem": "bike6.webp"},
    {"id": 7, "nome": "Bicicleta Ergométrica Spinning", "preco": 979.90, "imagem": "bike7.webp"},
    {"id": 8, "nome": "Bicicleta aro 29 KRW Alumínio", "preco": 792.30, "imagem": "bike8.webp"},
    {"id": 9, "nome": "Bicicleta GTSM1 MTB20", "preco": 1048.94, "imagem": "bike9.webp"},
]

# Rota para a página inicial
@app.route('/')
def paginainicial():
    return render_template('index.html')

# Rota para a página sobre
@app.route("/sobre", methods=('GET' ,))
def sobre():
    return render_template('sobre.html')


# Rota para o formulário de contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    feedback = None
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        # Criando o dicionário com os dados do contato
        contato_data = {
            'nome': nome,
            'email': email,
            'mensagem': mensagem
        }

        # Salvando os dados no arquivo JSON
        save_contato_to_file(contato_data)

        feedback = "Agradecemos por seu feedback. Fique de olho em seu email que logo entraremos em contato!"
    
    return render_template('contato.html', feedback=feedback)


@app.route('/produtos')
def produtos():
    return render_template('produtos.html', produtos=lista_produtos)

@app.route('/comprar/<int:produto_id>', methods=['GET', 'POST'])
def comprar(produto_id):
    produto = next((p for p in lista_produtos if p["id"] == produto_id), None)
    if produto:
        if request.method == 'POST':
            quantidade = int(request.form['quantidade'])
            valor_total = produto["preco"] * quantidade
            
            # Criando o dicionário com os dados da compra
            compra_data = {
                'produto_id': produto['id'],
                'nome_produto': produto['nome'],
                'quantidade': quantidade,
                'valor_total': valor_total
            }

            # Salvando a compra no arquivo JSON
            save_compra_to_file(compra_data)
            
            return render_template('comprar.html', produto=produto, compra_concluida=True, valor_total=valor_total, quantidade=quantidade)
        
        return render_template('comprar.html', produto=produto)
    return redirect(url_for('home'))

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

#--------------------BLOG-----------------#
