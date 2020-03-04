largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura*altura
qtdTinta = area/2
print('A área da parede é: {}m²'.format(area))
print('Você precisará de {} litros de tinta para pintar a parede'. format(qtdTinta))
