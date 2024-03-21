# views/produto_view.py
from meu_projeto.controllers.produto_controller import ProdutoController

class ProdutoView:
    def __init__(self):
        self.produto_controller = ProdutoController()

    def criar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        self.produto_controller.criar_produto(nome, preco, quantidade)

    def listar_produtos(self, perfil):
        produtos = self.produto_controller.listar_produtos()
        produtos_filtrados = [produto for produto in produtos if produto['perfil'] == perfil]
        for produto in produtos_filtrados:
            print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

    # Implemente métodos semelhantes para atualizar, buscar e deletar produtos conforme necessário.