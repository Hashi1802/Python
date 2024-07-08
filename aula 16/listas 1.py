valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um numero: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('cheguei ao final da lista')