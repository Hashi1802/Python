import random
p = input('Primeiro aluno: ')
s = input('segundo aluno: ')
t = input('terceiro aluno: ')
q = input('quarto aluno: ')
lista = [p, s, t, q]
random.shuffle(lista)
print('a ordem de apresentação será {}'.format(lista))