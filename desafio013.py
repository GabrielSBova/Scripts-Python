salario = float(input('Digite o seu salário R$'))
aumento = salario * (15 / 100)
salFinal = salario + aumento
print('O seu novo salario é de: R${:.2f}'.format(salFinal))
print('Porcentagem de aumento: 15%')

# OU

salario = float(input('Digite o salário do funcionário R$:'))
salNovo = salario + (salario * 15 / 100)
print('O funcionário que antes ganhava R${:.2f}, com 15% de aumento passa a receber R${:.2f}'.format(salario, salNovo))


