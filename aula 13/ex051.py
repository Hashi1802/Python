print('''{} 10 termos de uma PA {}
      '''.format(('=' * 10),('=' * 10)))
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print('{} '.format(c), end='-> ')
print('Acabou')