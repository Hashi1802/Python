lista = []
dados = []
decision = ''
max = min = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    decision = str(input('Deseja continuar ? [s/n] '))
    if len(lista) == 0:
        max = min = dados[1]
    else:
        if dados[1] > max:
            max = dados[1]
        if dados[1] < min:
            min = dados[1]
    lista.append(dados[:])
    dados.clear()
    if decision in 'nN':
        break
print('=_=' * 15)
print(f'Ao todo voce cadastrou {len(lista)} pessoas')
print(f'o maior peso foi de {max} kgs')
for p in lista:
    if p[1] == max:
        print(f'{p[0]}')
print(f'o menor valor foi de {min} kgs')
print(lista)