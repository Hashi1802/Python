frase = str(input('Digite uma frase: ')).strip().upper() ### strip removeu os espaço e o upper jogou tudo para maiusculo
palavras = frase.split() ###aqui separou as palavras em uma lista
junto = ''.join(palavras) ###aqui juntou essas palavras
inverso = ''
for letra in range(len(junto) -1, -1, -1): ###aqui inverteu as letras
    inverso += junto[letra]
if inverso == junto:
    print('{} escrito ao contrario é {} logo ele é um palindromo'.format(junto, inverso))
else:
    print('{} escrito ao contrario é {} logo ele NÃO é um palindromo'.format(junto, inverso))