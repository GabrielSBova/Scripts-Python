'''from math import trunc
num = float(input('Digite um número: '))
print('O número digitado é {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

#OU
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#OU SEM USAR BIBLIOTECAS:
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
