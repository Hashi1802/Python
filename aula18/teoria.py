def lin():
    print('-' * 40)


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def soma(a, b):
    s = a + b
    print(f'o valor da soma de {a} + {b} é {s}')


#Programa Principal
a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
soma(a, b)

###lin()
###print('Anderson Melo')
###lin() 
###titulo('Anderson Melo')
###titulo('el batorezao')
###titulo('Fofucho')