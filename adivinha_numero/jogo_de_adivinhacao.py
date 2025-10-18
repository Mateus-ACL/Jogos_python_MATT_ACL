import random
import pygame
import os
pygame.mixer.init()
tentativa = 0
cor = {'clean':'\033[m',
         'yellow':'\033[33m',
         'green':'\033[1;32m',
         'blue':'\033[1;34m',
         'purple':'\033[1;35m',
         'red':'\033[1;31m'}

base_dir = os.path.dirname(__file__)
som_vitoria = os.path.join(base_dir, 'victor.wav')
som_derrota = os.path.join(base_dir, 'derrota.wav')

while True:
    maquina_num = random.randint(1,5)
    print(f'{cor['yellow']}-=-'*18)
    entrada = int(input(f'{cor["clean"]}pensei em um número de {cor["green"]}1 a 5{cor["clean"]}, qual você acha que é? '))
    print(f'{cor['yellow']}-=-'*18)
    if entrada != maquina_num:
        print(f'{cor['red']}Não foi dessa vez')

        pygame.mixer.music.load(som_derrota) 
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    else :
        print(f'{cor['blue']}EXATAMENTE{cor['clean']}, você acertou')
        pygame.mixer.music.load(som_vitoria) 
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        break
    tentativa += 1
print(f'{cor['purple']}Você tentou {tentativa} vez(es)')