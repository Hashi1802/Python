n = eeee
p = 0
for c in range(0, n+1):
    if n % c == 0:
       print('\033[34m', end= '')
    else:
        print('\033[m', end= '')
    print('{}'.format(c), end= '')
