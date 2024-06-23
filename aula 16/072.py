cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 
        'oito', 'nove', 'dez', 'onze', 'doze' 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continua: ''
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f' voce digitou {cont[numero]}')
        continua = str(input('Voce quer continuar? '))
        if continua in 'Nn':
            break
        
