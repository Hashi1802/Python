s = 0
c = 0
for c in range (0,6, 1):
    p = int(input('Digite um Numero: '))
    if p % 2 == 0: 
        c += 1
        s += p
print('foram somados {} valores e o resultado foi {}'.format(c, s))
        