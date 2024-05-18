casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o valor do salario: '))
anos = float(input('Em quants anos pretende pagar: '))
mes = 12 * anos
parcela = (casa) / (mes)
print('Para pagar um casa de {} em {:.0f} anos a prestação será de R$ {:.2f}'.format(casa, anos, parcela))
if parcela < (30/100) * salario:
    print('Parabens, Seu emprestimo foi Aprovado!')
else:
    print('Reprovado')