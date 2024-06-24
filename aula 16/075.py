nume = (int(input('Digite um numero: ')),
        int(input('Digite Outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {nume}')
print(f'O valor 9 apareceu {nume.count(9)} vezes')#como contar em uma tupla
print(f'o valor 3 apareceu na {nume.index(3)} posição')#como saber a posição em uma tupla