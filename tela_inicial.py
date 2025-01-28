import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from Patrimonio import Patrimonio
from localizacao import Localizacao

class Tela_inicial(QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v = QVBoxLayout()
        
        self.label_titulo = QLabel ("Clicar para abrir a janela")
        # Botoes
        self.button = QPushButton("Abrir Patrimônio")
        self.button2 = QPushButton("Abrir Localizações")

        self.layout_v.addWidget(self.label_titulo)

        self.layout_v.addWidget(self.button)
        self.layout_v.addWidget(self.button2)
        
        self.button.clicked.connect(self.abrir_cadastro)
        self.button2.clicked.connect(self.abrir_local)

        self.setLayout(self.layout_v)

    def abrir_cadastro(self):
        self.pat = Patrimonio()
        self.pat.show()

    def abrir_local(self):
        self.pat = Localizacao()
        self.pat.show()
    
app = QApplication(sys.argv)
tela = Tela_inicial()
tela.show()
app.exec()