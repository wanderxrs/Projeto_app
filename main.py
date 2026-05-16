from flask import Flask, request, redirect, jsonify
import pymysql

app = Flask(__name__)


######################cadastro de itens###################
@app.route('/cadastrarItem', methods = ['POST'])
def cadastrarItem():
     
     #pegando dados do json
    dados = request.get_json()
    idFkUser = (dados['fkUser'])
    nomeProduto = str(dados['nomeProduto'])
    descProduto = str (dados['descProd'])
    precoProduto = (dados['precoProd'])

    #conectando com o banco
    banco = pymysql.connect(host="127.0.0.1", user="root", passwd="ny2005ny", database="database_projeto")
    cursor = banco.cursor()

    #fazendo o insert
    sql = "INSERT INTO products (user_id, name, description, price, created_at) VALUES (%s, %s, %s, %s, NOW());"

    #execultaltando o insert
    cursor.execute(sql, (idFkUser, nomeProduto, descProduto, precoProduto, ))
    banco.commit()
    banco.close()

    # status para ver no postman
    response = {'mensagem' : 'cadastro realizado', 'cod' : 200}
    return jsonify(response)


####################### EDITAR ######################################
@app.route('/editarItem', methods = ['PUT'])
def editaritem():

    dados = request.get_json()
    idRecebido = dados['id']
    nomeFunc = dados['nomeProduto']

    banco = pymysql.connect(host="127.0.0.1", user="root", passwd="ny2005ny", database="database_projeto")
    cursor = banco.cursor()

    sql = "UPDATE products set name = %s WHERE id = %s;"
    cursor.execute(sql, (nomeFunc, idRecebido, ))
    banco.commit()
    banco.close()
    response = {'mensagem' : 'Item atualizado', 'Codigo' : 200}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)