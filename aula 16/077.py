palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'prarticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palvra {p.upper( )} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')