import re
from flask import Flask, jsonify, request
from flask_cors import CORS
from analizador.analizador import AnalyzeType

app = Flask(__name__)
CORS(app, resources={r"/execute": {"origins": "*"}})


@app.route('/execute', methods=['GET'])
def execute():
    comando = request.args.get('comando')
    comando = re.sub(r"[#][^\n]*", "", comando)
    response = AnalyzeType(comando)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)