#! Python

with open('monroe.csv') as arquivo:
    for registro in arquivo:
        print(*registro.strip().split(','))