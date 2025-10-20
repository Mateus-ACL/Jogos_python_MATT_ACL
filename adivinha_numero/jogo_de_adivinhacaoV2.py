import random
import pygame
import os
import sys
from time import sleep


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
    while True:
        modo_jogo = str(input("""
Aperte [1] ou [2] para selecionar o modo de jogo:
[1] Tentativa erro: o número é redefinido a cada nova tentativa
[2] Modo de dicas: o número é o mesmo e é dado dicas até você acertar que número é

Aperte [M] ou [X] para utilizar funções do programa
[M] Insira 'M' na caixa de pergunta de número para voltar ao menu e selecionar um novo modo de jogo                                                             
[X] Insira 'X' em qualquer input para encerrar o programa
""")).strip().upper()
        if modo_jogo == 'X':
             sys.exit()
        if modo_jogo and modo_jogo.isnumeric():
            modo_jogo = int(modo_jogo[0])
            if modo_jogo <= 2:
                break
    #modo tentativa e erro
    if modo_jogo == 1:
        while True:
            maquina_num = random.randint(1,5)
            print(f'{cor['yellow']}-=-'*18)
            while True:
                entrada = str(input(f'{cor["clean"]}pensei em um número de {cor["green"]}1 a 5{cor["clean"]}, qual você acha que é? ')).upper().strip()
                if entrada == 'X':
                    print(f'{cor['yellow']}-=-'*18)
                    print(f'{cor['clean']}Finalizando programa',end='')
                    for c in range (0,3):
                        sleep(1)
                        print('.',end='')
                    sys.exit()
                if entrada == 'M':
                    break
                elif entrada and entrada.isnumeric():
                    print('Digite um número válido')
                    break
                entrada = int(entrada)
            print(f'{cor['yellow']}-=-'*18)
            if entrada != 'M':
                if entrada != maquina_num:
                    print(f'{cor['red']}Não foi dessa vez{cor['clean']}')
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
                tentativa += 1
            if entrada == 'M':
                break
    
    if modo_jogo == 2:
        print(f'{cor['yellow']}-=-'*18)
        maquina_num = random.randint(1,5)
        while True:
            entrada = str(input(f'{cor["clean"]}pensei em um número de {cor["green"]}1 a 5{cor["clean"]}, qual você acha que é? ')).upper().strip()
            if entrada == 'X':
                print(f'{cor['yellow']}-=-'*18)
                print(f'{cor['clean']}Finalizando programa',end='')
                for c in range (0,3):
                    sleep(1)
                    print('.',end='')
                sys.exit()
            if entrada == 'M':
                break
            elif not entrada.isnumeric():
                print('Digite um número válido')
                break
            entrada = int(entrada)
            print(f'{cor['yellow']}-=-'*18)
            if entrada != 'M':
                if entrada != maquina_num:
                    print(f'{cor['red']}Não foi dessa vez{cor['clean']}')
                    pygame.mixer.music.load(som_derrota) 
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        continue
                if entrada > maquina_num:
                    print('Você chutou alto')
                elif entrada < maquina_num:
                    print('Você chutou baixo')

                else :
                    print(f'{cor['blue']}EXATAMENTE{cor['clean']}, você acertou')
                    pygame.mixer.music.load(som_vitoria) 
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        continue
                    break
                tentativa += 1
                print(maquina_num)
        if entrada == 'M':
            break
            
print(f'{cor['purple']}Você tentou {tentativa} vez(es){cor['clean']}')
    
    