from flask import Flask, jsonify, request
#from flask.ext.sqlalchemy import SQLAlchemy

api_livros = Flask(__name__)

#Criar rota de integração para o banco de d


#Criar uma lista de dicionários aonde estára a referencia dos livros e também nomes de autores

livros = [
    {
        'id' : 1,
        'titulo' : 'O Senhor dos aneis - A Sociedade do Anel',
        'autor': 'J.R.R Tolken'
    },
    {
        'id': 2,
        'titulo' : 'Harry Potter e a Pedra Filosofial',
        'autor' : 'J.K Howling'

    },
    {
        'id' : 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos atômicos'
    }
]

# =============  Desenvolvimento das funçoes para cada EndPoint  ============

#EndPoint para Consultar todos os livros
@api_livros.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


#EndPoint para obter os livros através do ID
@api_livros.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
        return jsonify(livro)


#EndPoint para editar os livros através do ID
@api_livros.route('/livros/<int:id>', methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
       if livro.get('id') == id:
          livros[indice].update(livro_alterado)
          return jsonify(livros[indice])
       

#EndPoint para Criar e adicionar novos livros
@api_livros.route('/livros', methods=['POST'])
def incluir_novos_livros():
   novo_livro = request.get_json()
   livros.append(novo_livro)
   return jsonify(livros)

# EndPoint para excluir os livros pelo indíce
def excluir_livro(id):
   for indice, livro in enumerate(livros):
      if livro.get('id') == id:
         del livros[indice]
   return jsonify(livros)


api_livros.run(port=500, host='localhost', debug=True)