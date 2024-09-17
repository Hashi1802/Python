pessoa = dict()
pessoa['nome'] = str(input('nome: '))

while True:
    pessoa['sexo'] = str(input('Sexo: M/F ')).upper()[0]
    if pessoa['sexo'] in 'MF':
        break
    print('Erro! Digite apenas M ou F ')