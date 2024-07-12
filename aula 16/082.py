lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor? '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    decisao = str(input('Quer continuar? [S/N]'))
    if decisao in 'Nn':
        break
print('-=-' * 25)
print(f'a lista completa é {lista}')
print(f'a lista de pares é {par}')
print(f'A lista de impares é {impar}')