print('GERADOR DE PA')
print('-==-' * 4)
p = int(input('Primeiro Termo: '))
r = int(input('razao da PA: '))
termo = p
cont = 1
v = 1000
q = 10
while v != 0:
    while cont <= q:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('pausa')
    v = int(input('Quantos termos voce quer mostrar a mais? '))
    if v != 0:
        q += v
print('progressao finalizada com {} termos.'.format(cont - 1))
print('FIM')