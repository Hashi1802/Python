from math import factorial
n = int(input('Digite um numero para calcular o seu fatorial:'))
c = n #contador
f = 1 #fator nulo de multiplicação
print('calculando {}! '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='') #utilizando if e else em uma unica linha
    f *= c
    c -= 1 #contando de forma negativa
print('{}'.format(f))