def notas(*n, sit=False):
    """
    --> Função para avaliar notas e situações de varios alunos.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else: 
            r['situação'] = 'Ruim'
    return r


#programa principal
resp = notas(9, 10, 5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)