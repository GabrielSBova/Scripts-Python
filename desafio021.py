'''import pygame
pygame.init()
pygame.mixer.music.load('teminite_ascent_mp3_81470.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

#MÉTODO MAIS FUNCIONAL ABAIXO:

import pygame
pygame.mixer.init()
pygame.mixer.music.load('teminite_ascent_mp3_81470.mp3')
pygame.mixer.music.play()
input('Reproduzindo..')