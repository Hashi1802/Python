print('GERADOR DE PA')
print('-==-' * 4)
p = int(input('Primeiro Termo: '))
r = int(input('razao da PA: '))
termo = p
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')