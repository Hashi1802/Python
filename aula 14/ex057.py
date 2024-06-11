sexo = str(input('Informe seu sexo:[M/F] ')).lower()
while 'm' != sexo != 'f':
    sexo = str(input('que porra é {}? informe M ou F: '.format(sexo))).lower()
print('sexo {} registrado com sucesso.'.format(sexo))
