#MÉTODO 1
import random
import playsound

palpite = int(input('Descubra qual foi o número escolhido pelo computador, digite um número de 0 a 5: '))
numPC = int(random.randint(0, 5)) #FAZ O COMPUTADOR DIZER UM NÚMERO ENTRE 0 E 5
if palpite == numPC:
    print('Parabéns você acertou!')
    playsound.playsound('acerto mizeravi.mp3')
else:
    print('PC: Haha você errou! Eu pensei no número {} e não no {}!'.format(numPC, palpite))
    playsound.playsound('Errouu!.mp3')

#MÉTODO 2
from time import sleep
computador = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('-=-' * 20)
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
