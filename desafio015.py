qtdKm = float(input('Qual a quantidade de KMs percorridos com o carro alugado? '))
qtdDiasPerc = float(input('Por quantos dias o veículo foi alugado? '))
precoFinal = (60*qtdDiasPerc) + (0.15*qtdKm)
print('O preço a pagar pelo aluguel do carro é R${:.2f}'.format(precoFinal))
