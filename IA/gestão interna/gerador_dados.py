import pandas as pd
import random

# Gerar dados fictícios
num_amostras = 1000

# Lista de 10 nomes de motoristas
nomes_motoristas = ['João', 'Maria', 'Carlos', 'Ana', 'Pedro', 'Lucas', 'Sofia', 'Fernando', 'Beatriz', 'Gustavo']

tipos_veiculo = ['Moto', 'Carro', 'Van', 'Caminhão']
setores = [str(i) for i in range(100, 121)]  # Setores de 100 a 120
pontos_entrega_quantidade = [random.randint(5, 150) for _ in range(num_amostras)]  # Quantidade de pontos entre 5 e 150

# Gerando os dados
dados = {
    'Motorista': [random.choice(nomes_motoristas) for _ in range(num_amostras)],  # Substituindo números por nomes
    'Veículo': [random.choice(tipos_veiculo) for _ in range(num_amostras)],
    'Setor': [random.choice(setores) for _ in range(num_amostras)],  # Setores de 100 a 120
    'Ponto de Entrega': pontos_entrega_quantidade,  # Quantidade de pontos de entrega
    'Tempo de Entrega (minutos)': [random.randint(5, 60) for _ in range(num_amostras)]  # Tempo em minutos
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Salvar em um arquivo CSV com separador correto
df.to_csv('IA/dados_entrega.csv', index=False, sep=';', encoding='utf-8-sig')

print("Arquivo 'dados_entrega.csv' gerado com sucesso!")
