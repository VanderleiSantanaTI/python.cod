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
df = pd.read_csv('IA/dados_entrega.csv', sep=';')

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
    # Obter o valor selecionado do setor e pontos
    try:
        setor_escolhido = int(setor_entry.get())
        pontos_escolhidos = int(pontos_entry.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        return

    # Filtrar dados para o setor escolhido
    dados_filtrados = df[df['Setor'] == setor_escolhido].copy()

    # Verificar se o conjunto de dados filtrado está vazio
    if dados_filtrados.empty:
        messagebox.showerror("Erro", f"Não há dados para o setor {setor_escolhido}.")
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
    melhores_resultados = sorted(resultados, key=lambda x: x[2])

    # Limitar aos 5 melhores tempos
    melhores_resultados = melhores_resultados[:5]
  
    # Limpar o conteúdo atual da tabela
    for item in treeview.get_children():
        treeview.delete(item)

    # Adicionar os resultados na tabela
    motoristas = []
    veiculos = []
    tempos = []
    
    for motorista, veiculo, tempo_estimado in melhores_resultados:
        treeview.insert('', tk.END, values=(motorista, veiculo, f"{tempo_estimado:.2f}"))
        motoristas.append(motorista)
        veiculos.append(veiculo)
        tempos.append(tempo_estimado)
    
    # Criar gráfico de barras
    fig, ax = plt.subplots(figsize=(5, 4))
    
    # Garantir que os motoristas e os tempos estejam na mesma ordem (do menor para o maior tempo)
    ax.bar(motoristas, tempos, color='skyblue')
    ax.set_xlabel('Motoristas')
    ax.set_ylabel('Tempo Estimado (minutos)')
    ax.set_title(f'Tempos Estimados para o Setor {setor_escolhido}')
    
    # Exibir gráfico dentro da interface Tkinter
    for widget in frame_grafico.winfo_children():
        widget.destroy()  # Limpar o gráfico anterior
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)  # Tamanho do gráfico
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Criar a interface gráfica com Tkinter
root = tk.Tk()
root.title("Estimativa de Tempo de Entrega")

# Criar widgets
setor_label = tk.Label(root, text="Selecione o Setor:")
setor_label.pack(pady=5)

setor_entry = tk.Entry(root)
setor_entry.pack(pady=5)

pontos_label = tk.Label(root, text="Informe a quantidade de pontos:")
pontos_label.pack(pady=5)

pontos_entry = tk.Entry(root)
pontos_entry.pack(pady=5)

calcular_button = tk.Button(root, text="Calcular", command=estimar_tempo_entrega)
calcular_button.pack(pady=10)

# Criar uma tabela para exibir os resultados
treeview = ttk.Treeview(root, columns=("Motorista", "Veículo", "Tempo Estimado"), show="headings")
treeview.pack(pady=10)

# Definir as colunas
treeview.heading("Motorista", text="Motorista")
treeview.heading("Veículo", text="Veículo")
treeview.heading("Tempo Estimado", text="Tempo Estimado (minutos)")

# Ajustar a largura das colunas
treeview.column("Motorista", width=150)
treeview.column("Veículo", width=150)
treeview.column("Tempo Estimado", width=150)

# Frame para o gráfico
frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=10, fill=tk.BOTH, expand=True)

# Configurar o comportamento de fechamento
root.protocol("WM_DELETE_WINDOW", root.quit)

# Iniciar a interface gráfica
root.mainloop()
