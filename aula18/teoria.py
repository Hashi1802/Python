def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        return f

#programa principal

n = int(input('Digite um numero: '))
print(f'o fatorial de {n} é igual a {fatorial(n)}')