num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raizquad = num ** (1 / 2)
print('O número que você digitou é: {}'.format(num))
print('O dobro é: {} \nO triplo é: {}'.format(dobro, triplo))
print('A raiz quadrada é: {:.2f}'.format(raizquad))

# OU
num = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(num, (num * 2)))
print('O triplo de {} vale {}.'.format(num, (num * 3)))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num, (num ** (1 / 2))))

