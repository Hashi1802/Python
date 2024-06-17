idade = maioresde18 = homens = mulheres_menores_20 = 0
sexo = ''
continuar = 's'
while True:
    print('-' * 20)
    print('CADASTRO DE PESSOAS')
    print('-' * 20)
    idade = int(input('idade: '))
    if idade > 18:
        maioresde18 += 1
    sexo = str(input('Sexo: [M/F]')).lower().strip()[0]
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres_menores_20 += 1
    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()
    if continuar in 'Nn':
        break
print(f'o total de pessoas com mais de 18 anos é: {maioresde18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'e temos {mulheres_menores_20} com menos de 20 anos.')  