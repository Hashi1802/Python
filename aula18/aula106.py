def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('˜' * tam)
    print(f'  {msg}')
    print('˜' * tam)


#programa principal
comando = ''
while True:
    titulo('Sistema de Ajuda Python')
    comando = str(input("função ou biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')