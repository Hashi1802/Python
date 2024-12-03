import moeda
taxa = 10
preço = float(input("Digite o preço: "))
print(f'a Metade de R$ {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'o dobro de R$ {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'aumentando {taxa}%, temos {moeda.moeda(moeda.aumentar(preço, taxa))}')
print(f'diminuindo {taxa}%, temos {moeda.moeda(moeda.diminuir(preço, taxa))}')