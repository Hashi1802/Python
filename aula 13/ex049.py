n = int(input('Digite um numero para ver a tabuada: '))
c = 0
for c in range(0, 10, 1):
    c += 1
    r = n * c
    print('{} x {} = {}'.format(n, c, r))