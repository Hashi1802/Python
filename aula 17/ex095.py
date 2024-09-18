time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'quantos gols na partida {c} ?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:    
        resp = str(input('Quer continuar? [S/N] ')) .upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N')
    if resp == 'N':
        break
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-=' * 40)
for k, v in jogador.items():
    print(f' O Campo {k} tem o valor {v}')
print('-' * 40)
