n = 0
c = 0
s = 0
while n != 999:
    n = int(input('digite um número [999  para parar]' ))
    if n != 999:
        c +=1
        s += n
print('Voce digitou {} números e a soma entre eles foi {}'.format(c, s))