casa = float(input('Digite o valor da casa: '))
salComp = float(input('Digite o salário do comprador: '))
qtdAnos = int(input('Em quantos anos o comprador vai pagar? Digite: '))
parcela = casa / (qtdAnos*12)
prestMensal = 30/100 * salComp
if parcela > prestMensal:
    print('O valor da prestação mensal é: R${:.2f}'.format(parcela))
    print('ALERTA! Ultrapassado o valor de 30% do salário sobre a prestação mensal. Empréstimo NEGADO.')
else:
    print('O valor da prestação mensal é: R${:.2f}'.format(parcela))
    print('Empréstimo ACEITO!')
