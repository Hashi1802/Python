s = 0
maior = 0
nm = ''
id20 = 0
for c in range(1, 5):
    print(('{} pessoa'.format(c)))
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    sexo = str(input('sexo[M/F]: '))
    s += idade
    if sexo == m:
        if idade > maior:
            maior = idade
            nm = nome
    if sexo == f:
        if idade <= 20:
            id20 += 1
print('A média de idade do grupo é de {} anos.'.format((s / 4)))
print('o Homem mais velho tem {} anos e se chama {}'.format(maior, nm))
print('Ao todo são {} com menos de 20 anos'.format(id20))