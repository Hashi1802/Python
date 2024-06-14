while True:
    n = int(input('Digite um numero para ver a tabuada: '))
    if n < 0:
        break
    c = 0
    for c in range(1, 11, 1):
        r = n * c
        print('{} x {} = {}'.format(n, c, r))
print('Programa Tabuada Encerradp, volte sempre.')