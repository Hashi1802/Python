numeros = list ()
decisao = ''
while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor Duplicado!')
    decisao = str(input('Quer continuar? [S/N] ')).lower()
    if decisao in 'nN':
        break
print('-+' * 40)
print(f'Voce digitou os valores {numeros}')