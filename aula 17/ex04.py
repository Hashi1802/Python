galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: M/F ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F ')
    pessoa['idade'] = int(input('Digite sua idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer Continuar? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro Responda S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print(f'a) Ao todo eu tenho {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'b) A média de idade é de {media:5.2f}')
print('c) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('d) as pessoas que estão acima da méda')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f' {k} = {v}', end='')
        print()
print('>> ENCERRADO <<')