from random import randint
print(''' sou seu computador...
Acabei de pensar em um numero de 0 a 10.
Será que voce conegue adivinhar qual foi?
''')
c = randint(1,10)
ct = 0
p = 0
while p != c:
    p = int(input('Qual o seu palpite: '))
    if c > p:
        print('Mais... Tente novamente')
    if c < p:
        print('Menos... Tente novamente')
    ct += 1
print('Acertou com {} tentativas, Parabens!'.format(ct))