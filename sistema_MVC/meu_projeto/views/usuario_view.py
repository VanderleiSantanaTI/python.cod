# views/usuario_view.py
from meu_projeto.controllers.usuario_controller import UsuarioController

class UsuarioView:
    def __init__(self):
        self.usuario_controller = UsuarioController()

    def criar_usuario(self):
        nome = input("Digite o nome do usuário: ")
        senha = input("Digite a senha do usuário: ")
        self.usuario_controller.criar_usuario(nome, senha)

    def autenticar_usuario(self):
        nome = input("Digite o nome do usuário: ")
        senha = input("Digite a senha do usuário: ")
        usuario = self.usuario_controller.buscar_usuario_por_nome(nome)
        if usuario and usuario['senha'] == senha:
            return usuario
        else:
            print("Usuário ou senha incorretos.")
            return None
