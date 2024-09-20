def title(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def terreno(a, b):
    m = a * b
    print(f'a area de um terréno de {a} x {b} é {m}')


a = int(input('LARGURA (m):'))
b = int(input('COMPRIMENO (m): '))
title('Controle de Terreno')
terreno(a, b)