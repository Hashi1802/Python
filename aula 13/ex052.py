n = int(input('digite um numero: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
       print('\033[33m', end= '')
       t += 1
    else:
        print('\033[31m', end= '')
    print('{}'.format(c), end= '')
print(' \n\033[m O numero {} foi divisivel {} vezes'.format(n, t))
if t == 2:
    print('Sendo assim o {} é Primo'.format(n))
else:
    print('{} Não é primo'.format(n))
    