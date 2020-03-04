from os import lchmod

vel = float(input('Digite a velocidade do carro: '))
limite = vel - 80
multa = 7 * limite
print('A velocidade do carro é: {}Km/h'.format(vel))
if vel > 80:
    print('Você será multado por excesso de velocidade')
    print('A multa vai custar: R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

