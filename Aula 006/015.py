d = float(input('quantos dias de aluguel? '))
k = float(input('Quantos km rodados? '))
t = (d*60)+(k*0.15)
print('o Total a pagar é de R${:.2f}'.format(t))