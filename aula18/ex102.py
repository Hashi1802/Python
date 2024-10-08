def fatorial(n, show=False):
    """
    Calcula o Fatorial de um numero:
    para n: o numero a ser calculado.
    para show: (opcional) mostrar ou não a conta.
    return: o valor de um fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1: 
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


##print(fatorial(5, show=True))
help(fatorial)