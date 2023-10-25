import re
import os
import base64
from flask import Flask, jsonify, request
from flask_cors import CORS
from analizador.analizador import AnalyzeType
from comandos.login import verificar_credenciales


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/execute', methods=['GET'])
def execute():
    comando = request.args.get('comando')
    response = AnalyzeType(comando)
    return jsonify(response)

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return jsonify(verificar_credenciales(username, password))

@app.route('/getReportes', methods=['GET'])
def getReportes():
    lista_imagenes = os.listdir('./reportes')
    imagenes = [archivo for archivo in lista_imagenes if archivo.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    objetos_imagenes = []
    for imagen in imagenes:
        with open('./reportes/'+imagen, 'rb') as image_file:
            image_data = image_file.read()
            imagen_base64 = base64.b64encode(image_data).decode()
        
        objeto_imagen = {
            'nombre': imagen,
            'contenidoBase64': imagen_base64
        }
        objetos_imagenes.append(objeto_imagen)
    
    return jsonify({'imagenes': objetos_imagenes})


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000, debug = True)