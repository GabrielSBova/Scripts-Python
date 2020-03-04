from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo: '))
senAng = sin(radians(ang))
cosAng = cos(radians(ang))
tanAng = tan(radians(ang))
print('Seno de {}: {:.2f}'.format(ang, senAng))
print('Cosseno de {}: {:.2f}'.format(ang, cosAng))
print('Tangente de {}: {:.2f}'.format(ang, tanAng))
