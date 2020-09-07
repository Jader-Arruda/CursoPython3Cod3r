palavra = 'paralelepipedo'
for letra in palavra:

    print(letra, end = ',')

print('Fim')
 

aprovados = ['Rafaela','Pedro','Renato','Maria'] 
for nome in aprovados:
    print(nome)


for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)


dias_semana = ('Domingo','Segunda','Terca','Quarta','Quinta','Sexta','Sabado')

for num, dia in enumerate(dias_semana):
    print(f'{num+1}) - {dia}'.format(num,dia))


for letra in set('Muito legal'):
    print(letra)