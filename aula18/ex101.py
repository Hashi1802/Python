def voto():
    from datetime import date
    data = date.today().year
    pergunta = int(input('Em que ano voce nasceu? '))
    idade = data - pergunta
    print(idade)
    if idade <= 16:
        return f'com {idade} = não vota'
    elif 18 < idade < 70:
        return f'com {idade} = voto obrigatorio'
    else:
        return f'com {idade} = voto opcional'

voto()