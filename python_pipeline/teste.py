

import csv 
with open('monroe.csv') as arquivo:
    for registro in csv.reader(arquivo):
        print(*registro)