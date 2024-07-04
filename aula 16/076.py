listagem = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'transferidor', 4.20, 'compasso', 9.99, 'Mochila', 120.32, 'Canetas',22.30, 'livros', 34.90)
print('-' * 40)
print("LISTAGEM DE PREÇOS")
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)