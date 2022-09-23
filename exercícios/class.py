class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        lista_plano = ["basic", "premium"]
        
        if plano in lista_plano:
            self.plano = plano

        else:
            print("Plano inválido")
nomes = input("digite seunome: ")
cliente = Cliente(nomes, "lira@gmail.com", "premium")

print(cliente.nome)


print(f"Meu nome é : {cliente.nome} e meu email  é {cliente.email}")  

