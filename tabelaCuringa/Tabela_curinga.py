import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLineEdit,\
    QHBoxLayout, QHeaderView, QAbstractItemView, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TABELA PESQUISA - VSATECH")
        self.setGeometry(100, 100, 800, 600)

        # Conteúdo da lista com cabeçalhos "Placa", "Modelo", "Nome", "Status", "Categoria"
        self.data = [
            ["Placa", "Modelo", "Nome", "Status(ativo)", "Categoria"],
            ["ABC1234", "Onix", "Alice", "sim", "Carro"],
            ["DEF5678", "BMW", "Bob", "nao", "Moto"],
            ["GHI9101", "Sprinter", "Carol", "sim", "Van"],
            ["JKL1123", "Volvo", "David", "nao", "Ônibus"],
            ["MNO4567", "Mercedes", "Eva", "sim", "Caminhão"],
            ["PQR7890", "Fiat 500", "Fabiana", "sim", "Carro"],
            ["STU1234", "Harley-Davidson Street 750", "George", "sim", "Moto"],
            ["VWX5678", "Renault Kangoo", "Helena", "sim", "Van"],
            ["YZA9012", "Scania K360", "Igor", "nao", "Ônibus"],
            ["BCD3456", "Ford Cargo 2429", "Julia", "sim", "Caminhão"],
            ["EFG6789", "Chevrolet Cruze", "Karen", "sim", "Carro"],
            ["HIJ2345", "Yamaha MT-07", "Lucas", "nao", "Moto"],
            ["KLM4567", "Citroën Jumper", "Mariana", "sim", "Van"],
            ["NOP8901", "Volvo B450R", "Nelson", "nao", "Ônibus"],
            ["QRS5678", "Volvo FH16", "Olivia", "sim", "Caminhão"],
            ["TUV1234", "Hyundai HB20", "Paulo", "sim", "Carro"],
            ["WXY9012", "Ducati Panigale V4", "Renata", "nao", "Moto"],
            ["ZAB3456", "Mercedes-Benz Sprinter 415", "Sandra", "sim", "Van"],
            ["CDE6789", "Marcopolo Paradiso 1800 DD", "Thiago", "nao", "Ônibus"],
            ["FGH2345", "Scania R500", "Ursula", "sim", "Caminhão"],
            ["IJK4567", "Toyota Corolla", "Victor", "sim", "Carro"],
            ["LMN8901", "Kawasaki Ninja ZX-10R", "Wanda", "nao", "Moto"],
            ["OPQ5678", "Peugeot Partner", "Xavier", "sim", "Van"],
            ["RST1234", "Irizar i8", "Yasmin", "nao", "Ônibus"],
            ["UVW9012", "Volvo FH540", "Zeca", "sim", "Caminhão"],
            ["XYZ3456", "Honda Civic", "Ana", "sim", "Carro"],
            ["BCD6789", "Suzuki GSX-R1000", "Bruno", "sim", "Moto"],
            ["EFG2345", "Ford Transit", "Clara", "sim", "Van"],
            ["HIJ5678", "Man Lion's Coach", "Daniel", "nao", "Ônibus"],
            ["KLM9012", "Mercedes-Benz Actros", "Elisa", "sim", "Caminhão"],
            ["NOP3456", "Fiat Palio", "Fernanda", "sim", "Carro"],
            ["QRS6789", "Triumph Bonneville T100", "Gabriel", "nao", "Moto"],
            ["TUV2345", "Renault Master", "Heloisa", "sim", "Van"],
            ["WXY5678", "Neobus Thunder+", "Isaac", "nao", "Ônibus"],
            ["ZAB9012", "Volvo FH440", "Jéssica", "sim", "Caminhão"],
            ["CDE3456", "Volkswagen Gol", "Kevin", "sim", "Carro"],
            ["FGH6789", "BMW S1000RR", "Laura", "nao", "Moto"],
            ["IJK2345", "Mercedes-Benz Vito", "Miguel", "sim", "Van"],
            ["LMN5678", "Irizar i6S", "Natália", "nao", "Ônibus"],
            ["OPQ9012", "Volvo FMX", "Otávio", "sim", "Caminhão"],
            ["RST3456", "Chevrolet Onix", "Patrícia", "sim", "Carro"],
            ["UVW6789", "Kawasaki Z900", "Quitéria", "nao", "Moto"],
            ["XYZ2345", "Fiat Doblo", "Roberto", "sim", "Van"],
            ["BCD5678", "Neoplan Skyliner", "Sofia", "nao", "Ônibus"],
            ["EFG9012", "Scania G410", "Tadeu", "sim", "Caminhão"]
        ]

        # Configurar o widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Criar a tabela
        self.table = QTableWidget()
        layout.addWidget(self.table)

        # Configurar a tabela
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        # Estilo do cabeçalho
        header = self.table.horizontalHeader()
        header.setStyleSheet("background-color: rgb(255,0,0);")
        header.setStyleSheet("font:20px")

        # Tornar a tabela responsiva
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Estilo intercalado para o corpo da tabela
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet("alternate-background-color: lightgray;")

        # Criar a linha de filtros
        self.filter_layout = QHBoxLayout()
        layout.addLayout(self.filter_layout)
        self.filters = []

        # Label para exibir o total de resultados
        self.total_label = QLabel()
        layout.addWidget(self.total_label)
        self.total_label.setStyleSheet("font:15px")
        self.load_data()

    def load_data(self):
        # Definir o número de linhas e colunas
        self.table.setRowCount(len(self.data) - 1)  # -1 to exclude header
        self.table.setColumnCount(len(self.data[0]))

        # Configurar os cabeçalhos
        self.table.setHorizontalHeaderLabels(self.data[0])

        # Preencher a tabela com os dados
        for row_index, row_data in enumerate(self.data[1:]):  # Skip the header
            for col_index, item in enumerate(row_data):
                cell_item = QTableWidgetItem(item)
                cell_item.setFlags(cell_item.flags() ^ Qt.ItemIsEditable)  # Remover a flag de edição
                self.table.setItem(row_index, col_index, cell_item)

        # Adicionar filtros para cada coluna
        for col_index in range(len(self.data[0])):
            filter_edit = QLineEdit()
            filter_edit.setPlaceholderText(self.data[0][col_index])
            filter_edit.textChanged.connect(lambda text, col=col_index: self.apply_filter(text, col))
            filter_edit.setStyleSheet("color: rgb(0,0,0);font: 15px")  # Definir o estilo do texto
            self.filter_layout.addWidget(filter_edit)
            self.filters.append(filter_edit)


    def apply_filter(self, text, col):
        total_results = 0
        for row in range(self.table.rowCount()):
            item = self.table.item(row, col)
            if text.lower() in item.text().lower():
                self.table.showRow(row)
                total_results += 1
            else:
                self.table.hideRow(row)
        # Atualizar o total de resultados após filtrar
        self.total_label.setText(f"Total de resultados encontrados: {total_results}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
