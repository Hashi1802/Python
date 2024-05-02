from math import radians, sin, cos, tan
a = float(input('digite o angulo: '))
sen = sin(radians(a))
print('o angulo {} tem o SENO de {:.2f}'.format(a, sen))
cos = cos(radians(a))
print('o angulo {} tem o COSENO de {:.2f}'.format(a, cos))
tan = tan(radians(a))
print('o angulo {} tem a TANGENTE de {:.2f} '.format(a, tan))