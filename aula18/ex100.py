from random import randint
from time import sleep
def sorteia(lista):
    """teste"""
    print('SORTEANDO 5 VALORES DA LISTA ', end='')
    for cont in range(1, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ',end='', flush=True)
        sleep(0.3)
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os valores pares de {lista} temos {soma}')

numeros = list()
help(sorteia)