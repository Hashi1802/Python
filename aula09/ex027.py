n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
##a função slipt fatia o nome em padaços separados por espaço##
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu segundo nome é {}'.format(nome[1]))
print('Seu terceiro nome é {}'.format(nome[len(nome)-1]))