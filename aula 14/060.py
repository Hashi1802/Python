n = int(input('''
Digite um numero para
calcular o seu fatorial: 
'''
))
p = n - 1
while p != 1:
    f = n * p
    print('{} = {} x {}'.format(n, p, f))
 