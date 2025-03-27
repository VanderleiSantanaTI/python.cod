import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Carregar os dados do arquivo CSV
df = pd.read_csv('dados_entrega.csv', sep=';')

# Codificar variáveis categóricas 'Motorista', 'Veículo' e 'Setor' com LabelEncoder
encoder_motorista = LabelEncoder()
df['Motorista Codificado'] = encoder_motorista.fit_transform(df['Motorista'])

encoder_veiculo = LabelEncoder()
df['Veículo Codificado'] = encoder_veiculo.fit_transform(df['Veículo'])

encoder_setor = LabelEncoder()
df['Setor Codificado'] = encoder_setor.fit_transform(df['Setor'])

# Criar a coluna de produtividade (pontos / tempo)
df['Produtividade'] = df['Ponto de Entrega'] / df['Tempo de Entrega (minutos)']

# Atributos preditores: motorista, veículo, setor e produtividade
X = df[['Setor Codificado', 'Motorista Codificado', 'Veículo Codificado', 'Produtividade']]

# Variável alvo: Tempo de entrega
y = df['Tempo de Entrega (minutos)']

# Dividir os dados em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

def estimar_tempo_entrega(setor_escolhido, tipo_veiculo_escolhido, pontos_escolhidos):
    # Filtrar dados para o setor e tipo de veículo escolhido
    dados_filtrados = df[(df['Setor'] == setor_escolhido) & (df['Veículo'] == tipo_veiculo_escolhido)].copy()

    # Verificar se o conjunto de dados filtrado está vazio
    if dados_filtrados.empty:
        print(f"Não há dados para o setor {setor_escolhido} e veículo {tipo_veiculo_escolhido}.")
        return

    # Criar uma lista para armazenar os resultados
    resultados = []

    # Iterar sobre cada linha do dataframe filtrado para estimar o tempo de entrega
    for _, row in dados_filtrados.iterrows():
        motorista = row['Motorista']
        veiculo = row['Veículo']
        # Calcular a produtividade para o motorista/veículo no setor
        produtividade_motorista_veiculo = row['Produtividade']
        
        # Estimar o tempo de entrega com base na quantidade de pontos e produtividade
        tempo_estimado = pontos_escolhidos / produtividade_motorista_veiculo
        
        # Adicionar o resultado à lista
        resultados.append((motorista, veiculo, tempo_estimado))
    
    # Ordenar os resultados pelos tempos estimados, em ordem crescente
    melhores_resultados = sorted(resultados, key=lambda x: x[2])[:5]

    # Exibir os 5 menores tempos estimados
    print(f"\nOs 5 melhores tempos estimados para o setor {setor_escolhido} com o veículo {tipo_veiculo_escolhido} e {pontos_escolhidos} pontos:")
    for motorista, veiculo, tempo_estimado in melhores_resultados:
        print(f"Tempo estimado para o motorista {motorista}, veículo {veiculo}: {tempo_estimado:.2f} minutos")

# Exemplo de uso: Estimar os 5 melhores tempos para o setor 106 com o tipo de veículo 'Moto' e 50 pontos
setor_escolhido = 105
tipo_veiculo_escolhido = 'carro'  # Pode ser 'Moto', 'Carro', 'Van' ou 'Caminhão'
pontos_escolhidos = 50
estimar_tempo_entrega(setor_escolhido, tipo_veiculo_escolhido, pontos_escolhidos)
