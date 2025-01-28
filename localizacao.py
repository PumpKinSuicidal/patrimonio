from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout;
import sys

class Localizacao(QWidget):
    def __init__(self): 
        super().__init__()

        self.setGeometry(10,30,500,500)

        self.setWindowTitle("Cadastro de Localização.")

        self.layout_v = QVBoxLayout()

        # ID
        self.label_id = QLabel("ID:")
        self.label_id.setStyleSheet("Qlabel.{Font-size:12pt}")
        # ID
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QlineEdit{font-size:12pt}")

        # Empresa
        self.label_empresa = QLabel("Empresa:")
        self.label_empresa.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Empresa
        self.edit_empresa = QLineEdit()
        self.edit_empresa.setStyleSheet("QlineEdit{font-size:12pt}")

        # Logradouro
        self.label_logradouro = QLabel("Logradouro:")
        self.label_logradouro.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Logradouro
        self.edit_logradouro = QLineEdit()
        self.edit_logradouro.setStyleSheet("QlineEdit{font-size:12pt}")

        # Número
        self.label_numero = QLabel("Número:")
        self.label_numero.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Número
        self.edit_numero = QLineEdit()
        self.edit_numero.setStyleSheet("QlineEdit{font-size:12pt}")

        # Prédio
        self.label_predio = QLabel("Prédio:")
        self.label_predio.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_predio = QLineEdit()
        self.edit_predio.setStyleSheet("QlineEdit{font-size:12pt}")

        # Andar
        self.label_andar = QLabel("Andar:")
        self.label_andar.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_andar = QLineEdit()
        self.edit_andar.setStyleSheet("QlineEdit{font-size:12pt}")

        # Sala
        self.label_sala = QLabel("Sala:")
        self.label_sala.setStyleSheet("Qlabel.{Font-size:12pt}")
        # Line Edit
        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QlineEdit{font-size:12pt}")

        # Botão
        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:yellow;color:black;font-size:12pt;font-weight:bold}")

        self.button.clicked.connect(self.cadastrar)

        
        # adicionar ID
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)        

        # adicionar empresa
        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_empresa)

        # adicionar logradouro
        self.layout_v.addWidget(self.label_logradouro)
        self.layout_v.addWidget(self.edit_logradouro)

        # adicionar numero
        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)

        # adicionar predio
        self.layout_v.addWidget(self.label_predio)
        self.layout_v.addWidget(self.edit_predio)

        # adicionar andar
        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)

        # adicionar sala
        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)

        # Adicionar botão
        self.layout_v.addWidget(self.button)

        # Adicionar o layout_v na tela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        # Criar uma variavel que fará referencia ao arquivo de texto
        # encoding="utf-8" pra colocar acentuação
         arquivo = open("clientes.txt","+a", encoding="utf-8")
         arquivo.write(f"ID: {self.edit_id.text()}\n")
         arquivo.write(f"Empresa: {self.edit_empresa.text()}\n")
         arquivo.write(f"Logradouro: {self.edit_logradouro.text()}\n")
         arquivo.write(f"Número: {self.edit_numero.text()}\n")
         arquivo.write(f"Prédio: {self.edit_predio.text()}\n")
         arquivo.write(f"Andar: {self.edit_andar.text()}\n")
         arquivo.write(f"Sala: {self.edit_sala.text()}\n")
         arquivo.write("------------------------------------------\n")
         arquivo.close()