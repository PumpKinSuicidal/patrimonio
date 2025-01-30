from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox;
import sys
import csv

class LocalizarPatrimonio(QWidget):
    def __init__(self): 
        super().__init__()

        self.setGeometry(10,30,500,500)

        self.setWindowTitle("Localizar Patrimônio.")

        self.layout_v = QVBoxLayout()

        # ID
        self.label_id = QLabel("ID:")
        self.label_id.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QlineEdit{font-size:12pt}")

        # Número de Série 
        self.label_serie = QLabel("Número de Série:")
        self.label_serie.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QlineEdit{font-size:12pt}")

        # Nome do Patrimônio
        self.label_nome = QLabel("Nome do Patrimônio:")
        self.label_nome.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QlineEdit{font-size:12pt}")

        # Tipo do Patromônio
        self.label_tipo = QLabel("Tipo do Patromônio:")
        self.label_tipo.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QlineEdit{font-size:12pt}")

        # Descrição
        self.label_desc = QLabel("Descrição")
        self.label_desc.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_desc = QLineEdit()
        self.edit_desc.setStyleSheet("QlineEdit{font-size:12pt}")

        # Localização
        self.label_loc = QLabel("Localização:")
        self.label_loc.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_loc = QLineEdit()
        self.edit_loc.setStyleSheet("QlineEdit{font-size:12pt}")

        # Data de Fabricação
        self.label_fab = QLabel("Data de Fabricação:")
        self.label_fab.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_fab = QLineEdit()
        self.edit_fab.setStyleSheet("QlineEdit{font-size:12pt}")

        # Data de aquisição
        self.label_aqui = QLabel("Data de aquisição:")
        self.label_aqui.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_aqui = QLineEdit()
        self.edit_aqui.setStyleSheet("QlineEdit{font-size:12pt}")
        
        # adicionar ID
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)    
        # Adicionar botão de achar o ID
        self.btnbuscar = QPushButton("Buscar Patrimônio") 
        self.layout_v.addWidget(self.btnbuscar) 
        self.btnbuscar.clicked.connect(self.localizar)   
         

        # adicionar Número de Série 
        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)

        # adicionar Nome do Patrimônio
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        # adicionar Tipo do Patromônio
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        # adicionar Descrição
        self.layout_v.addWidget(self.label_desc)
        self.layout_v.addWidget(self.edit_desc)

        # adicionar Localização
        self.layout_v.addWidget(self.label_loc)
        self.layout_v.addWidget(self.edit_loc)

        # adicionar Data de Fabricação
        self.layout_v.addWidget(self.label_fab)
        self.layout_v.addWidget(self.edit_fab)

        # adicionar Data de aquisição
        self.layout_v.addWidget(self.label_aqui)
        self.layout_v.addWidget(self.edit_aqui)

        # Adicionar o layout_v na tela
        self.setLayout(self.layout_v)
    # Abrir o arquivo CSV e atribuir a uma variavel
    def localizar(self):
        arquivo = open("clientes.csv","r",encoding="utf8")
        linhas = csv.reader(arquivo)

        for i in linhas:
            lin = str(i).replace("['", "").replace("']", "").split(";")
        if(lin[0] == self.edit_id.text):
            self.edit_serie.setText(lin[1])
            self.edit_nome.setText(lin[2])
            self.edit_tipo.setText(lin[3])
            self.edit_desc.setText(lin[4])
            self.edit_loc.setText(lin[5])
            self.edit_fab.setText(lin[6])
            self.edit_aqui.setText(lin[7])
# app = QApplication(sys.argv)
# # Instncia da classe cadastro cliente para iniciar a janela
# tela = Patrimonio()
# # Exibir a tela durante a execução
# tela.show()
# # Ao clicar no botão fechar a tela deve fechar e sair da memória
# app.exec()
