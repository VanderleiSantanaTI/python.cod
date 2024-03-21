# controllers/usuario_controller.py
from meu_projeto.models.usuario_model import UsuarioModel


class UsuarioController:
    def __init__(self):
        self.usuario_model = UsuarioModel()

    def criar_usuario(self, nome, senha):
        self.usuario_model.criar_usuario(nome, senha)

    def buscar_usuario_por_nome(self, nome):
        return self.usuario_model.buscar_usuario_por_nome(nome)
