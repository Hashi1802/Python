def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro digite um numero inteiro valido!\033[m')
        if ok:
            break
    return valor


#Programa Principal
n = leiaint('digite um numero: ')
print(f'voce acabou de digitar o numero {n}')