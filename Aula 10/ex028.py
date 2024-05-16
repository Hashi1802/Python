from random import randint
from time import sleep
computador = randint(0,5)
num = int(input('Estou sorteando um premio incrivel Escolha um numero entre 0 e 5: '))
print('Boa sorte!')
print('processando...')
sleep(5)
if num == computador:
    print('Parabens Voce ganhou a oportunidade de cair de boca na minha piroca!')
else:
    print('sinto muito nao foi dessa vez.')

