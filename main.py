from flask import Flask, request, redirect, jsonify
import pymysql
from routes.registro_login import carregar_rotas

app = Flask(__name__)

carregar_rotas(app)

######################cadastro de itens###################
@app.route('/cadastrarItem', methods = ['POST'])
def cadastrarItem():
     
     #pegando dados do json
    dados = request.get_json()
    idFkUser = (dados['fkUser'])
    nomeProduto = str(dados['nomeProduto'])
    descProduto = str (dados['descProd'])
    precoProduto = (dados['precoProd'])

    #conectando com o bd
def db():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',         
        password='12345678',
        database='database_projeto', 
        cursorclass=pymysql.cursors.DictCursor 
    )


    cursor = bd.cursor()

    #fazendo o insert
    sql = "INSERT INTO products (user_id, name, description, price, created_at) VALUES (%s, %s, %s, %s, NOW());"

    #execultaltando o insert
    cursor.execute(sql, (idFkUser, nomeProduto, descProduto, precoProduto, ))
    bd.commit()
    bd.close()

    # status para ver no postman
    response = {'mensagem' : 'cadastro realizado', 'cod' : 200}
    return jsonify(response)


####################### EDITAR ######################################
@app.route('/editarItem', methods = ['PUT'])
def editaritem():
    #pegando valores do json
    dados = request.get_json()
    idRecebido = dados['id']
    nomeFunc = dados['nomeProduto']

    bd = pymysql.connect(host="127.0.0.1", user="root", passwd="ny2005ny", database="database_projeto")
    cursor = bd.cursor()
    #update no bd
    sql = "UPDATE products set name = %s WHERE id = %s;"
    cursor.execute(sql, (nomeFunc, idRecebido, ))
    bd.commit()
    bd.close()
    response = {'mensagem' : 'Item atualizado', 'Codigo' : 200}
    return jsonify(response)


###########remover itens#################################
@app.route('/excluirItens', methods = ['DELETE'])
def excluir():
    dados = request.get_json()
    idRecebido = dados['id']

    bd = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "ny2005ny", database= "database_projeto")
    cursor = bd.cursor()

    sql = "DELETE FROM products WHERE ID = %s;"
    cursor.execute(sql, (idRecebido, ))

    bd.commit()
    bd.close()

    response = {'Resposta' : 'Item deletado', 'cod' : 200}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)