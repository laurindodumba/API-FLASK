from flask import Flask, make_response, jsonify, request
from bd import carros



app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# =========== Rota para buscar todos os carros que estão listados no banco de dados ============
@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify( 
            message='Lista de Carros.',
            dados=carros
    )
) 

# ============  Rota para criar os novos carros ======================= 
@app.route('/carros', methods=['POST'])
def create_carros():
    carro = request.json
    carros.append(carro)
    return make_response(
        jsonify(
            message='Carros criados com Sucesso!',
              dados=carro
        )
    )
app.run()
