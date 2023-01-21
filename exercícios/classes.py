class Carro:
    def __init__(self,marca,modelo,cor,ligar=False):
        self.marca=marca
        self.modelo = modelo
        self.cor=cor
        self.ligar=ligar
        
    def veiculo(self):
        return f'{self.marca} - {self.modelo} na cor {self.cor}'    
        
    def ligarCarro(self):
        if self.ligar:
            print(f'[LIGAR]- O carro {self.modelo} ja esta ligado.')
            return
        print(f'[LIGAR]- O carro {self.modelo} foi ligado.')
        self.ligar = True
    
    def  desligarCarro(self):
        if not self.ligar:
            print(f'[DESLIGAR]-O carro {self.modelo} ja esta desligado')
            return
        print(f'[DESLIGAR]- O carro {self.modelo} foi desligado.')
        self.ligar = False

        
 
        





c1=Carro('Fiat','Uno','Prata')
c2=Carro('Fiat','Argo', 'preto')
c3=Carro('Renault','Kwid','Branco')
c4=Carro('Volkswagen', 'Fox','Amarelo')
c5=Carro('Chevrolet','Onix 1.4', 'Preto')


c3.ligarCarro()
c3.ligarCarro()
c3.desligarCarro()
c3.desligarCarro()
c2.ligarCarro()
c1.desligarCarro()
c2.desligarCarro()
c3.desligarCarro()


