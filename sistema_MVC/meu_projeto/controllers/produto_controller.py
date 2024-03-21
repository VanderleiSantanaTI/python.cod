# controllers/produto_controller.py
from meu_projeto.models.produto_model import ProdutoModel


class ProdutoController:
    def __init__(self):
        self.produto_model = ProdutoModel()

    def criar_produto(self, nome, preco, quantidade):
        self.produto_model.criar_produto(nome, preco, quantidade)

    def listar_produtos(self):
        return self.produto_model.listar_produtos_model()

    # Implemente métodos semelhantes para atualizar, buscar e deletar produtos conforme necessário.