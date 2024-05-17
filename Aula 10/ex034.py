sal = float(input('Digite o valor do salario: R$'))
if sal <= 1250:
    v1 = sal * 1.15
    print('Voce recebeu um aumento salarial de 15%, seu novo salario é de R$ {:.2f}'.format(v1))
else:
    v2 = sal * 1.10
    print('voce recebeu um aumento de 10%, seu novo salario é de R${:.2f}'.format(v2))