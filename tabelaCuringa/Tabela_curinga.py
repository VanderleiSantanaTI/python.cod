import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLineEdit,\
    QHBoxLayout, QHeaderView, QAbstractItemView, QLabel
import pyautogui
class MainWindow(QMainWindow):
    def __init__(self, data):
        self.data = data
        super().__init__()

        self.setWindowTitle("TABELA PESQUISA - VSATECH")
        # uso do pyautogui.size()[0]/2) para abrir a janela no meio
        self.setGeometry(int(pyautogui.size()[0]/2)-400, int(pyautogui.size()[1]/2)-300, 800, 600)

        # Conteúdo da lista com cabeçalhos "Placa", "Modelo", "Nome", "Status", "Categoria"

        #self.data = []

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
        try:
            self.load_data()
        except Exception as e:
            self.total_label.setText("Sem entradas de dados 'self.data = []'")
            print(e)

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
