from datetime import datetime
dados = dict()
dados['nome'] = str(input('nome: '))
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem):'))
if dados != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados ['contratação'] + 35) - datetime.now().year)
print('-=-' * 30)
print(dados)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}')