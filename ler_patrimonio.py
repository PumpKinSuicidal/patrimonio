import csv

# Abrir o arquivo CSV e atribuir a uma variavel
arquivo = open("clientes.csv","r",encoding="utf8")
linhas = csv.reader(arquivo)

for i in linhas:
    lin = str(i).replace("['", "").replace("']", "").split(";")
    if(lin[0]=="28"):
        print(lin)