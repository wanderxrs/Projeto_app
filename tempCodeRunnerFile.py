from flask import Flask, request, redirect, jasonify
import pymysql

app = Flask(__name__)



@app.route('/cadastrarItem', methods = ['POST'])
def cadastrarItem():
    
    dados = request.get_json()
    idFkUser = (dados['fkUser'])
    nomeProduto = str(dados['nomeProduto'])
    descProduto = str (dados['descProd'])
    precoProduto = (dados['precoProd'])



    banco = pymysql.connect(host="127.0.0.1", user="root", passwd="12345678", database="database_projeto")
    cursor = banco.cursor()


    sql = "INSERT INTO products (user_id, name, description, price, created_at) VALUES (%s, %s, %s, %s, NOW());"


    cursor.execute(sql, (nomeProduto, idFkUser, descProduto, precoProduto, ))
    banco.commit()
    banco.close()


    response = {'mensagem' : 'cadastro realizado', 'cod' : 200}
    return jasonify(response)

if __name__ == "__main__":
    app.run(debug=True)