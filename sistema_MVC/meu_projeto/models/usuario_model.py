# models/usuario_model.py
import sqlite3



class UsuarioModel:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY,
                                nome TEXT,
                                senha TEXT,
                                perfil TEXT
                            )''')  # Adicionando a coluna "perfil" à tabela
        self.conn.commit()

    def criar_usuario(self, nome, senha):
        self.cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        self.conn.commit()

    def buscar_usuario_por_nome(self, nome):
        self.cursor.execute("SELECT id, nome, senha, perfil FROM usuarios WHERE nome=?", (nome,))
        usuario = self.cursor.fetchone()
        if usuario:
            return {'id': usuario[0], 'nome': usuario[1], 'senha': usuario[2], 'perfil': usuario[3]}
        else:
            return None
