lista = []
maior_valor = 0
posicao_maior = ''
menor_valor = 9999
posicao_menor = ''
for c in range(5):
    lista.append(int(input(f'Digite um Valor para a posição {c}: ')))
    if lista[c] > maior_valor:
        maior_valor = lista[c]
        posicao_maior = c
    if lista[c] < menor_valor:
        menor_valor = lista[c]
        posicao_menor = c
print('=-=' * 20)
print(f'voce digitou os valores {lista}')
print(f'o maior valor digitado foi {maior_valor} na posição {posicao_maior}')
print(f'o menor valor digitado é {menor_valor} na posição {posicao_menor}')