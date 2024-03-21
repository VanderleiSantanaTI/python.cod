# models/produto_model.py
from meu_projeto.models.usuario_model import UsuarioModel
import sqlite3


class ProdutoModel:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                                id INTEGER PRIMARY KEY,
                                nome TEXT,
                                preco REAL,
                                quantidade INTEGER,
                                perfil TEXT
                            )''')  # Adicionando a coluna "perfil" à tabela
        self.conn.commit()


    def criar_produto(self, nome, preco, quantidade):
        self.cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
        self.conn.commit()

    def listar_produtos_model(self):
        self.cursor.execute("SELECT id, nome, preco, quantidade, perfil FROM produtos")
        produtos = self.cursor.fetchall()
        produtos_dicionario = []
        for produto in produtos:
            produto_dicionario = {
                'id': produto[0],
                'nome': produto[1],
                'preco': produto[2],
                'quantidade': produto[3],
                'perfil': produto[4]
            }
            produtos_dicionario.append(produto_dicionario)
        return produtos_dicionario


    # Implemente métodos semelhantes para atualizar, buscar e deletar produtos conforme necessário.