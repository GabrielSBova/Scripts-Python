dist = float(input('Digite a distância da viagem: '))
print('Distância: {} Km'.format(dist))
preco1 = dist*0.50
preco2 = dist*0.45
if dist<=200:
    print('Preço da passagem: R${:.2f}'.format(preco1))
else:
    print('Preço da passagem: R${:.2f}'.format(preco2))

#if simplificado abaixo
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} Km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))


