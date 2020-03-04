from math import hypot
catO = float(input('Digite o comprimento do cateto oposto do triângulo: '))
catAd = float(input('Digite o comprimento do cateto adjacente do triângulo: '))
hipo = hypot(catO, catAd)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipo))




