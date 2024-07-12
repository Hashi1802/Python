lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    decision = str(input('Deseja continuar? '))
    if decision in 'Nn':
        break
cinco = (5 in lista)
if cinco == True:
    print('o Valor 5 foi encontrado na lista!')
else:
    print('o valor 5 nao foi encontrado na lista')
print('-=-' * 30)
print(f'voce digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(lista)