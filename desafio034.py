salario = float(input('Digite o seu salário: '))
aumento1 = (10 / 100) * salario
aumento2 = (15 / 100) * salario
if salario > 1250:
    print('O seu aumento é de R${:.2f}, com isso seu salário passa a ser R${:.2f}'.format(aumento1, (salario+aumento1)))
else:
    print('O seu aumento é de R${:.2f}, com isso seu salário passa a ser R${:.2f}'.format(aumento2, (salario+aumento2)))
