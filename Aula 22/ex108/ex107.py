import moeda
taxa = 10
preço = float(input("Digite o preço: "))
print(f'a Metade de R$ {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'o dobro de R$ {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'aumentando {taxa}%, temos {moeda.aumentar(preço, taxa, True)}')
print(f'diminuindo {taxa}%, temos {moeda.diminuir(preço, taxa, True)}')