sexo = str(input('Informe seu sexo:[M/F] ')).lower().strip()
while sexo not in 'MmFf':
    sexo = str(input('que porra é {}? informe M ou F: '.format(sexo))).lower()
print('sexo {} registrado com sucesso.'.format(sexo))
