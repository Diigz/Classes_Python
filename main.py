# Método simples:
import os
import time
from classes import CaixaDeSom

os.system('cls')

print(f'ESSE É O MÉTODO UTILIZANDO SOMENTE IF:\n')

def comparador(volume_atual):
    volume_alto = 100
    if volume_atual == volume_alto:
        print(
            f'Atualmente você está no volume {volume_atual}% então é o máximo que podemos chegar.')
    elif volume_atual < volume_alto:
        print(
            f'Você está {volume_atual}% do volume, para estar no máximo falta {volume_alto-volume_atual}%')

print(comparador(20))
time.sleep(3.0)
os.system('cls')

# -------------------------------------------------------------------------------------------------------------------------------------

# Método complexo:
print(f'ESSE É O MÉTODO UTILIZANDO CLASSES:\n')

print(f'Essa é a 1º Caixa de som:')
caixaDeSom_1 = CaixaDeSom()
caixaDeSom_1.Comparador(20)

print(f'Essa é a 2º Caixa de som:')
caixaDeSom_2 = CaixaDeSom()
caixaDeSom_2.Comparador(100)

time.sleep(3.0)
input('\nAperte qualquer tecla para encerrar...')