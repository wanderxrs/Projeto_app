from flask import Flask, request, redirect, jsonify
import pymysql
from routes.registro_login import carregar_rotas

app = Flask(__name__)

carregar_rotas(app)

# 1. Função de conexão isolada (Mude a senha aqui se necessário para o seu banco)
def db():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',         
        password='ny2005ny',  # Deixei a senha padronizada, ajuste se for '12345678'
        database='database_projeto', 
        cursorclass=pymysql.cursors.DictCursor 
    )

###################### CADASTRO DE ITENS ###################
@app.route('/cadastrarItem', methods=['POST'])
def cadastrarItem():
    dados = request.get_json()
    idFkUser = dados['fkUser']
    nomeProduto = str(dados['nomeProduto'])
    descProduto = str(dados['descProd'])
    precoProduto = dados['precoProd']

    # Conectando usando a função db()
    conexao = db()
    cursor = conexao.cursor()

    # Fazendo o insert
    sql = "INSERT INTO products (user_id, name, description, price, created_at) VALUES (%s, %s, %s, %s, NOW());"
    cursor.execute(sql, (idFkUser, nomeProduto, descProduto, precoProduto))
    
    conexao.commit()
    cursor.close()
    conexao.close()

    response = {'mensagem': 'cadastro realizado', 'cod': 200}
    return jsonify(response)


####################### EDITAR ######################################
@app.route('/editarItem', methods=['PUT'])
def editaritem():
    dados = request.get_json()
    idRecebido = dados['id']
    nomeFunc = dados['nomeProduto']

    conexao = db()
    cursor = conexao.cursor()
    
    sql = "UPDATE products set name = %s WHERE id = %s;"
    cursor.execute(sql, (nomeFunc, idRecebido))
    
    conexao.commit()
    cursor.close()
    conexao.close()
    
    response = {'mensagem': 'Item atualizado', 'Codigo': 200}
    return jsonify(response)


########### REMOVER ITENS #################################
@app.route('/excluirItens', methods=['DELETE'])
def excluir():
    dados = request.get_json()
    idRecebido = dados['id']

    conexao = db()
    cursor = conexao.cursor()

    sql = "DELETE FROM products WHERE ID = %s;"
    cursor.execute(sql, (idRecebido,))

    conexao.commit()
    cursor.close()
    conexao.close()

    response = {'Resposta': 'Item deletado', 'cod': 200}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)