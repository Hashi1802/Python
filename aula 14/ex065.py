n = s = c = m = 0
d = ''
maior = 1
menor = 999999999
while d != 'n':
    n = int(input('Digite um numero: '))
    c += 1
    s += n
    m = s / c
    d = str(input('Voce deseja continuar? [s/n]')).lower()
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('voce digitou {} numeros e a media foi {:.2f}'.format(c, m))
print('o maior valor foi {} e o menor valor foi {}'.format(maior, menor))