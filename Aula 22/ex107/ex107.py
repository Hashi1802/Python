import moeda
taxa = 10
preço = float(input("Digite o preço: "))
print(f'a Metade de R$ {preço} é {moeda.metade(preço)}')
print(f'o dobro de R$ {preço} é R${moeda.dobro(preço)}')
print(f'aumentando {taxa}%, temos R$ {moeda.aumentar(preço, taxa)}')
print(f'diminuindo {taxa}%, temos R${moeda.diminuir(preço, taxa)}')