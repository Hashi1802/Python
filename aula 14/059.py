from time import sleep
p = int(input('Primeiro Valor: '))
s = int(input('Segundo Valor: '))
soma = 0
o = 0
multi = 0
while o != 5:
    o = int(input(''' 
                  [ 1 ]somar
                  [ 2 ] multiplicar
                  [ 3 ] maior
                  [ 4 ] novos numeros
                  [ 5 ] sair do programa

>>>> qual é a opção?  '''))
    if o == 1:
        soma = p + s
        print('A soma entre {} e {} é {}'.format(p, s, soma))
        print('=-==' * 10)
    elif o == 2:
        multi = p * s
        print('a multiplicação entre {} e {} é {}'.format(p, s, multi))
        print('=-==' * 10) 
    elif o == 3:
        if p > s:
            print('entre {} e {} o maior valor é {}'.format(p, s, p))
            print('=-==' * 10) 
        elif p < s:
            print('entre {} e {} o maior valor é {}'.format(p, s, s))
            print('=-==' * 10) 
    elif o == 4:
        p = int(input('Primeiro Valor: '))
        s = int(input('Segundo Valor: '))
    elif o == 5:
        print('Finalizando...')
        sleep(1)

    else:
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE')
print('FINALIZANDO...')
print('FIM DO PROGRAMA! VOLTE SEMPRE')