#! Python


import csv

with open('cepea-consulta.csv') as entrada:
    dados = entrada.read()

    for registro in dados.splitlines():
        print('{}'.format(*registro[0:8]).split(';'))
    