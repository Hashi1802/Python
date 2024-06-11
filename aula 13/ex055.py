maior = 0
menor = 100000000
for c in range(1, 6):
    peso = float(input('digite o peso da {} pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('o maior peso lido foi {} kg'.format(maior))
print('O menor peso lido foi {} kg'.format(menor))