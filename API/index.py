from flask import Flask, request, jsonify
import requests
from users import *


app = Flask(__name__)

@app.route("/ver", methods=["GET"])
def ver_usuario_todos():
    return jsonify(ver_usuario())


@app.route("/ver/<int:id>", methods=["GET"])
def busca_usuario_id(id):
    bruto = ver_usuario_id(id)
    if bruto != None:
        dicionario = {
        'id': bruto[0],
        "name": bruto[1],
        "senha": bruto[2],
    }
        return jsonify(dicionario)
    else: 
        return {"mensagem": "ERRO! ID não localizado!"}
    

@app.route("/register/<name>/<senha>", methods=["POST"] )
def register(name, senha):
    return jsonify(criar_usuario(name, senha))


@app.route("/login/<name>/<senha>", methods=["POST"])
def logar(name, senha):
    return login(name, senha)

if __name__ == "__main__":
    app.run(port=5050, host="localhost", debug=True)