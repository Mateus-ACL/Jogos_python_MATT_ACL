import random

itens = ('pedra', 'papel', 'tesoura')

i = int(input("""
1: pedra
2: papel
3: tesoura
"""))

m = random.randint(1,3)

#empate
if i == m :
    print('Ambos jogaram {} e empataram'.format(itens[i-1]))

#vitoria
elif i == 1 and m == 3 :
    print('Jogador jogou pedra e ganhou')
elif i == 2 and m == 1 :
    print('Jogador jogou papel e ganhou')
elif i == 3 and m == 2 :
    print('Jogador jogou tesoura e ganhou')

#derrota
elif i == 1 and m == 2 :
    print('Jogador jogou pedra e perdeu')
elif i == 2 and m == 3 :
    print('Jogador jogou papel e perdeu')
elif i == 3 and m == 1 :
    print('Jogador jogou tesoura e perdeu')
