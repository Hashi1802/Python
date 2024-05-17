num = float(input('digite quantos km é a sua viagem: '))
v1 = num * 0.50
v2 = num * 0.45
print('voce esta prestes a começar a sua viagem de {} km'.format(num))
if num <= 200:
    print('O preço da sua passagem é R$ {}'.format(v1))
else:
    print('O preço da sua passagem é R$ {}'.format(v2))


