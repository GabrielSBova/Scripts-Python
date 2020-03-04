preco = float(input('Digite o preço do produto R$:'))
desconto = preco*(5/100)
precoFinal = preco - desconto
print('O novo preço do produto é: {:.2f}'.format(precoFinal))

#OU

preco = float(input('Qual é o preço do produto? R$'))
novoPreco = preco - (preco*5/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novoPreco))


