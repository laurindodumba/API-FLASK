from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

api_livros = Flask(__name__)

#api_livros.config['SQLALCHEMY_DATABASE_URI'] = '127.0.0.1 +pymysql://3306 + root'  # Adicione a conexão com o banco de dados correta
api_livros.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://api:127.0.0.1/api'

db = SQLAlchemy(api_livros)

class Livros(db.Model):
    __tablename__ = 'livros'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100))
    autor = db.Column(db.String(50))

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor



# Crie uma lista de objetos Livros em vez de dicionários
livros = [
    Livros(titulo='O Senhor dos Anéis - A Sociedade do Anel', autor='J.R.R Tolkien'),
    Livros(titulo='Harry Potter e a Pedra Filosofal', autor='J.K Rowling'),
    Livros(titulo='Hábitos Atômicos', autor='James Clear')
]

@api_livros.route('/livros', methods=['GET'])
def obter_livros():
    livros = Livros.query.all()
    return jsonify([{'id': livro._id, 'titulo': livro.titulo, 'autor': livro.autor} for livro in livros])

@api_livros.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    livro = Livros.query.get(id)
    if livro:
        return jsonify({'id': livro._id, 'titulo': livro.titulo, 'autor': livro.autor})
    return jsonify({'message': 'Livro não encontrado'}), 404

@api_livros.route('/livros/<int:id>', methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    livro = Livros.query.get(id)
    if livro:
        livro.titulo = livro_alterado.get('titulo', livro.titulo)
        livro.autor = livro_alterado.get('autor', livro.autor)
        db.session.commit()
        return jsonify({'id': livro._id, 'titulo': livro.titulo, 'autor': livro.autor})
    return jsonify({'message': 'Livro não encontrado'}), 404

@api_livros.route('/livros', methods=['POST'])
def incluir_novos_livros():
    novo_livro = request.get_json()
    livro = Livros(titulo=novo_livro.get('titulo'), autor=novo_livro.get('autor'))
    db.session.add(livro)
    db.session.commit()
    return jsonify({'id': livro._id, 'titulo': livro.titulo, 'autor': livro.autor}), 201

@api_livros.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    livro = Livros.query.get(id)
    if livro:
        db.session.delete(livro)
        db.session.commit()
        return jsonify({'message': 'Livro excluído com sucesso'})
    return jsonify({'message': 'Livro não encontrado'}), 404

if __name__ == '__main__':
    with api_livros.app_context():
        db.create_all()
    api_livros.run(port=5000, host='localhost', debug=True)
