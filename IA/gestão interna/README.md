# Sistema de Estimativa de Tempo de Entrega

Este é um sistema para estimar tempos de entrega baseado em dados históricos, utilizando machine learning.

## Requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone ou baixe este repositório

2. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

## Como Executar

1. Certifique-se de que você tem um arquivo `entregas.csv` no mesmo diretório do programa, com as seguintes colunas:
   - Motorista
   - Veículo
   - Setor
   - Ponto de Entrega
   - Tempo de Entrega (minutos)

2. Execute o programa:
```bash
python modelo_interface.py
```

## Uso
1. Selecione o setor desejado
2. Informe a quantidade de pontos de entrega
3. Selecione o tipo de veículo
4. Clique em "Calcular" para ver as estimativas

O sistema mostrará os 5 melhores motoristas para a rota e um gráfico comparativo dos tempos estimados. 