print('=' * 30)
print('{:30}'.format('Banco ASM'))
print('=' * 30)
valor = int(input('Que valor quer sacar? '))
total = valor
ced = 50
total_cedulas = 0
while True:
    if total >= ced:
        total -= ced
        total_cedulas += 1
    else:
        print(f'Total de {total_cedulas} cédulas de R$ {ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_cedulas = 0
        if total == 0:
            break
