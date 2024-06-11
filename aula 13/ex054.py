from datetime import date  ###importando a biblioteca de data
atual = date.today().year ### importando a data atual.
maior = 0
menor = 0
for c in range(1,8):
    p = int(input('Em que ano a {} pessoa nasceu?'.format(c)))
    if (atual - p) >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('e tambem tivemos {} menores de idade'.format(menor))