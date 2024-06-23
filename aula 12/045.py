from random import randint
from time import sleep
print('Pedra, Papel e Tesoura')
print('Sua opções:')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
p = int(input('Qual sua jogada? '))
print('-='* 11)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-='*10)
c = randint(1, 3) 
if p == 1:
    if c == 1:
        print('Empate')
    elif c == 2:
         print('voce perdeu')
    elif c == 3:
        print ('')
elif p == 2:
    if c == 1:
        print('voce ganhou')
    elif c == 2:
        print('empatou')
    elif c == 3:
        print('voce perdeu')
elif p == 3:
    if c == 1:
        print('Voce perdeu')
    elif c == 2:
        print('Voce Ganhou')
    elif c ==3:
        print('empatou') 