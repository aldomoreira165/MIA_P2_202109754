import re
from flask import Flask, jsonify, request
from flask_cors import CORS
from analizador.analizador import AnalyzeType
from comandos.login import verificar_credenciales

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/execute', methods=['GET'])
def execute():
    comando = request.args.get('comando')
    comando = re.sub(r"[#][^\n]*", "", comando)
    response = AnalyzeType(comando)
    return jsonify(response)

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return jsonify(verificar_credenciales(username, password))


if __name__ == '__main__':
    app.run(debug=True)