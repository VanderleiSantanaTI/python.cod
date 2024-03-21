# main.py
from meu_projeto.views.produto_view import ProdutoView
from meu_projeto.views.usuario_view import UsuarioView


def main():
    usuario_view = UsuarioView()
    usuario_autenticado = usuario_view.autenticar_usuario()

    if usuario_autenticado:
        perfil_usuario = usuario_autenticado['perfil']  # Corrigir aqui
        perfil_usuario2 = usuario_autenticado['nome']  # Corrigir aqui
        # print(perfil_usuario2)
        while True:
            print("0. Criar usuário")
            print("1. Criar produto")
            print("2. Listar produtos")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == "0":
                usuario_view.criar_usuario()
            elif opcao == "1":
                produto_view = ProdutoView()
                produto_view.criar_produto()
            elif opcao == "2":
                produto_view = ProdutoView()
                produto_view.listar_produtos(perfil_usuario)
                print(perfil_usuario2)
            elif opcao == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Usuário não autenticado. Encerrando.")


if __name__ == "__main__":
    main()

# Para criar um Login administrador
# import sqlite3
# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
#                         id INTEGER PRIMARY KEY,
#                         nome TEXT,
#                         senha TEXT,
#                         perfil TEXT
#                     )''')  # Adicionando a coluna "perfil" à tabela
# conn.commit()
# nome = "admin"
# senha = 999393
# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()
# cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
# conn.commit()
