print('-='*20)
print('Analisador de Triangulo')
print('-='*20)
r1 = float(input('Primeiro seguimento'))
r2 = float(input('Segundo Seguimento'))
r3 = float(input('Terceiro Seguimento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
     print('os seguimentos acima podem forma um triangulo')
else:
     print('os seguimentos acima não podem forma um triangulo ')