#! Python

arquivo = open('pessoas.csv')

try:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

finally:
    print('Finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo ja foi fechado')