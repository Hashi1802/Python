n = float(input('preço das compras:'))
print('[1]à vista dinheiro')
print('[2] 1x no cartão')
print('[3] 2x no cartão')
print('[4] 3x no cartão')
o = int(input('Digite a opção de pagamento: '))
if o == 1:
    v = n * 0.9
    print('sua compra de R$ {} vai custar R$ {} no final.'.format(n, v))
elif o == 2:
    v = n * 0.95
    print('sua compra de R$ {} vai custar R$ {} no final.'.format(n, v))
elif o == 3:
    print('Sua compra vai custar R$ {}'.format(n))
elif o == 4:
    v = n * 1.2
    p = int(input('Quantas parcelas: '))
    vp = v / p
    print('sua Compra de R$ {} vai custar R$ {}, o valor da parcela fica {}'.format(n, v, vp))
    
else:
    print('Erro! tente novamente')