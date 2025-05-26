from flask import Flask, request, jsonify, render_template
import csv
import os
import webbrowser
import threading

app = Flask(__name__)
CSV_FILE = 'entregas.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    data = request.json

    linha = [
        data['motorista'],
        data['veiculo'],
        data['setor'],
        data['ponto'],
        data['tempo']
    ]

    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Motorista', 'Veículo', 'Setor', 'Ponto de Entrega', 'Tempo de Entrega (minutos)'])
        writer.writerow(linha)

    return jsonify({'status': 'ok'})

def abrir_navegador():
    webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == '__main__':
    threading.Timer(1, abrir_navegador).start()
    app.run(debug=False)
