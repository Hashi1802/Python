print('-' * 20)
print('LOJÃO SUPER BARATO')
print('-' * 20)
produto = ''
preco = soma = produtos_maiores_mil = 0
continuar = ''
produto_mais_barato = ''
preço_mais_barato = 9999999
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    continuar = str(input('Quer Continuar ? [S/N]')).lower().split()[0]
    soma += preco
    if preco > 1000:
        produtos_maiores_mil += 1
    if preco < preço_mais_barato:
        produto_mais_barato = produto
        preço_mais_barato = preco
    if continuar in 'Nn':
        break
print(f'O total da compra foi {soma}')
print(f'temos {produtos_maiores_mil} custando mais de RS 1000.00')
print(f'o produto mais barato foi {produto_mais_barato} que custa {preço_mais_barato}')


