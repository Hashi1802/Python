a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = b
if a>b and a>c:
    maior = a
if c>a and c>b:
    maior = c
print('o menor valor digitado é {}'.format(menor))
print('o maior valor digitado é {}'.format(maior))
