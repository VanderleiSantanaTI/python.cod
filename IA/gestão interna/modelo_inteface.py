import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Carregar os dados do arquivo CSV
df = pd.read_csv('entregas.csv', sep=',')

def converter_minutos_em_horas(minutos):
    # Separar a parte inteira (minutos) e a parte decimal (fração de minutos)
    minutos_inteiros = int(minutos)
    segundos = (minutos - minutos_inteiros) * 60  # Converte a parte decimal para segundos
    
    # Calcular as horas, minutos e segundos
    horas = minutos_inteiros // 60
    minutos_restantes = minutos_inteiros % 60
    segundos_restantes = round(segundos)  # Arredondar os segundos para o número inteiro mais próximo
    
    # Formatar no formato "hh:mm:ss" com 2 casas para cada valor
    return f"{str(horas).zfill(2)}:{str(minutos_restantes).zfill(2)}:{str(segundos_restantes).zfill(2)}"



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

def estimar_tempo_entrega():
    # Obter os valores selecionados do setor, tipo de veículo e pontos
    try:
        setor_escolhido = int(setor_entry.get())
        tipo_veiculo_escolhido = veiculo_combobox.get()
        pontos_escolhidos = int(pontos_entry.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        return

    # Filtrar dados para o setor e tipo de veículo escolhido
    dados_filtrados = df[(df['Setor'] == setor_escolhido) & (df['Veículo'] == tipo_veiculo_escolhido)].copy()

    # Verificar se o conjunto de dados filtrado está vazio
    if dados_filtrados.empty:
        messagebox.showerror("Erro", f"Não há dados para o setor {setor_escolhido} e veículo {tipo_veiculo_escolhido}.")
        return

    # Criar um dicionário para armazenar os motoristas e os tempos mínimos
    motoristas_dict = {}

    # Iterar sobre cada linha do dataframe filtrado para estimar o tempo de entrega
    for _, row in dados_filtrados.iterrows():
        motorista = row['Motorista']
        veiculo = row['Veículo']
        # Calcular a produtividade para o motorista/veículo no setor
        produtividade_motorista_veiculo = row['Produtividade']
        
        # Estimar o tempo de entrega com base na quantidade de pontos e produtividade
        tempo_estimado = pontos_escolhidos / produtividade_motorista_veiculo
        
        # Verificar se o motorista já foi adicionado ao dicionário
        if motorista not in motoristas_dict or motoristas_dict[motorista] > tempo_estimado:
            motoristas_dict[motorista] = tempo_estimado

    # Ordenar os motoristas pelo tempo estimado, do menor para o maior
    melhores_resultados = sorted(motoristas_dict.items(), key=lambda x: x[1])

    # Limitar aos 5 melhores tempos
    melhores_resultados = melhores_resultados[:5]
  
    # Limpar o conteúdo atual da tabela
    for item in treeview.get_children():
        treeview.delete(item)

    # Adicionar os resultados na tabela
    motoristas = []
    veiculos = []
    tempos = []
    
    for motorista, tempo_estimado in melhores_resultados:
        # Encontrar o veículo correspondente ao motorista
        veiculo = dados_filtrados[dados_filtrados['Motorista'] == motorista]['Veículo'].iloc[0]
        
        treeview.insert('', tk.END, values=(motorista, veiculo, f"{converter_minutos_em_horas(tempo_estimado)}"))
        motoristas.append(motorista)
        veiculos.append(veiculo)
        tempos.append(tempo_estimado)
    
    # Criar gráfico de barras
    fig, ax = plt.subplots(figsize=(5, 4))
    
    # Garantir que os motoristas e os tempos estejam na mesma ordem (do menor para o maior tempo)
    ax.bar(motoristas, tempos, color='skyblue')
    ax.set_xlabel('Motoristas')
    ax.set_ylabel('Tempo Estimado (minutos)')
    ax.set_title(f'Tempos Estimados para o Setor {setor_escolhido} com {tipo_veiculo_escolhido}')
    
    # Exibir gráfico dentro da interface Tkinter
    for widget in frame_grafico.winfo_children():
        widget.destroy()  # Limpar o gráfico anterior
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)  # Tamanho do gráfico
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    root.geometry("1000x500")
    
# Criar a interface gráfica com Tkinter
root = tk.Tk()
root.title("Estimativa de Tempo de Entrega")

# Definir a largura mínima e altura mínima da janela
root.geometry("480x500")
root.minsize(480, 500)

# Frame principal (centralizado)
frame_principal = tk.Frame(root)
frame_principal.pack(fill="both", expand=True)

# Criar o frame para o layout lado a lado
frame_lado_a_lado = tk.Frame(frame_principal)
frame_lado_a_lado.pack(fill="both", expand=True)

# Criar o frame para a tabela
frame_tabela = tk.Frame(frame_lado_a_lado, width=300)
frame_tabela.pack(side="left", fill="both", expand=True, padx=10)

# Criar o frame para o gráfico
frame_grafico = tk.Frame(frame_lado_a_lado, width=400)
frame_grafico.pack(side="left", fill="both", expand=True, padx=10)

# Criar widgets dentro do frame da tabela (esquerda)
setor_label = tk.Label(frame_tabela, text="Selecione o Setor:")
setor_label.pack(pady=5)

setor_entry = tk.Entry(frame_tabela)
setor_entry.pack(pady=5)

pontos_label = tk.Label(frame_tabela, text="Informe a quantidade de pontos:")
pontos_label.pack(pady=5)

pontos_entry = tk.Entry(frame_tabela)
pontos_entry.pack(pady=5)

# ComboBox para seleção do tipo de veículo
veiculo_label = tk.Label(frame_tabela, text="Selecione o Tipo de Veículo:")
veiculo_label.pack(pady=5)

veiculos = ['Moto', 'Carro', 'Van', 'Caminhão']
veiculo_combobox = ttk.Combobox(frame_tabela, values=veiculos)
veiculo_combobox.set('Moto')  # valor inicial
veiculo_combobox.pack(pady=5)

calcular_button = tk.Button(frame_tabela, text="Calcular", command=estimar_tempo_entrega)
calcular_button.pack(pady=10)

# Criar uma tabela para exibir os resultados
treeview = ttk.Treeview(frame_tabela, columns=("Motorista", "Veículo", "Tempo Estimado"), show="headings")
treeview.pack(pady=10)

# Definir as colunas
treeview.heading("Motorista", text="Motorista")
treeview.heading("Veículo", text="Veículo")
treeview.heading("Tempo Estimado", text="Tempo Estimado (minutos)")

# Ajustar a largura das colunas
treeview.column("Motorista", width=150)
treeview.column("Veículo", width=100)
treeview.column("Tempo Estimado", width=200)

# Configurar o comportamento de fechamento
root.protocol("WM_DELETE_WINDOW", root.quit)

# Iniciar a interface gráfica
root.mainloop()
