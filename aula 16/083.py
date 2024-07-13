exp = str(input('Digite sua expressão: '))
pilha = []
c1 = 0
c2 = 0
for simb in exp:
    if simb == '(':
        c1 += 1
        pilha.append('(')
    elif simb == ')':
        c2 += 1
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão esta valida')
else:
    print('sua expressão esta errada.')
if c1 == c2:
    print('tava que essa porra tava certa!')
elif c1 != c2:
    print('essa misera ficou muito mais simples')