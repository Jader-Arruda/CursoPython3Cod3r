"""for i in range(1,11):
    if i == 5:
        continue
    print(i)
else:
    print('fim')"""

from random import randint

def sortear_dado():
    return randint(1,6)


for i in range(1,7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('Acertou miserávi',i)
        break
        
            
else:
    print('Nao acertou. O numero e ',i,' e voce chutou ',sortear_dado())
