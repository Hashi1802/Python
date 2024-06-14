from random import randint
print('-=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-' * 20)
p = s = c = v = d =  0
e = ''
pi = ''
res = ''
while True:
    if d == 1:
        break
    p = int(input('Digite um valor: '))
    print('-=-' * 20)
    while e not in 'PpIi':
        e = str(input('par ou impar ? [p/i] ')).lower().upper[0]
    if e == 'p':
        e = 'par'
    elif e != p:
        e = 'impar'
    print('-=-' * 20)
    c = randint(0, 11)
    s = p + c
    if s % 2 == 0: 
        pi = ('par')
    if s % 2 !=0:
        pi = ('impar')
    print(f'voce jogou {p} e o computador jogou {c}. o Total de {s} deu {pi} ')
    if e == pi:
        res = ('VENCEU')
        v += 1
        print('Voce Venceu')
    elif e != pi:
        res = ('Perdeu')
        d += 1
        print('Voce Perdeu.') 
    print('-=-' * 20)
print(f'Game Over venceu {v} vezes. ')
print('-=-' * 20)
    
        

