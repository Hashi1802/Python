s = 0
maior = 0
nm = ''
contfem = 0
m = 'm'
f = 'f'
for c in range(1, 5):
    print(('----- {} pessoa -----'.format(c)))
    nome = str(input('nome: ')).strip() ###remover os espaços
    idade = int(input('idade: '))
    sexo = str(input('sexo[M/F]: '))
    s += idade
    if sexo in 'Mm':
        if idade > maior:
            maior = idade
            nm = nome
    if sexo in 'Ff':
        if idade <= 20:
            contfem += 1
print('A média de idade do grupo é de {} anos.'.format((s / 4)))
print('o Homem mais velho tem {} anos e se chama {}'.format(maior, nm))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contfem))