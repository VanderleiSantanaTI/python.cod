import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from main import Main

class TelaCadastro(QMainWindow):
    def __init__(self):
        super(TelaCadastro, self).__init__()
        uic.loadUi('tela_cadastro.ui', self)  # Carregar o arquivo .ui

        self.btnCancelar2.clicked.connect(self.open_table_window)


    def open_table_window(self):
        TelaCadastro.close(self)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaCadastro()
    window.show()
    sys.exit(app.exec_())
