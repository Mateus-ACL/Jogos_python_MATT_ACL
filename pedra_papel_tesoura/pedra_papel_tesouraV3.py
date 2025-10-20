import random
from time import sleep

cor = {'clean':'\033[m',
         'yellow':'\033[33m',
         'green':'\033[1;32m',
         'blue':'\033[1;34m',
         'purple':'\033[1;35m',
         'red':'\033[1;31m'}
itens = ('pedra', 'papel', 'tesoura')
print(f'{cor['yellow']}▲▼'*13 )
print(f'{'PEDRA , PAPEL , TESOURA':^26}')
print('▲▼'*13)
print('vamos jogar',end='')
#limpando formatação
print(f'{cor["clean"]}',end='')
empate = vitoria = derrota =0

while True:
    while True:
        opcao = str(input("""
ESCOLHA:
[1]: pedra
[2]: papel
[3]: tesoura
"""))
        if opcao and opcao.isnumeric():
            opcao = int(opcao[0])
            if opcao > 3:
                print('Escolha uma opção entre 1 e 3')
                sleep(2)
            elif opcao <= 3:
                break
        else:
            print('escolha uma opção númerica entre 1 e 3')
            sleep(2)
    
    pc = random.randint(1,3)
    print('='*20)
    print('Jogador jogou {}'.format(itens[opcao-1]))
    print('Maquina jogou {}'.format(itens[pc-1]))
    print('='*20)

    if opcao == 1:
        if pc == 1:
            print(f'{cor['purple']}EMPATE')
            empate += 1
        elif pc == 2:
            print(f'{cor['red']}Maquina venceu')
            derrota += 1
        elif pc == 3:
            print(f'{cor['green']}Jogador venceu')
            vitoria += 1
    if opcao == 2:
        if pc == 1:
            print(f'{cor['red']}Maquina venceu')
            derrota += 1
        elif pc == 2:
            print(f'{cor['purple']}EMPATE')
            empate += 1
        elif pc == 3:
            print(f'{cor['green']}Jogador venceu')
            vitoria += 1
    if opcao == 3:
        if pc == 1:
            print(f'{cor['red']}Maquina venceu')
            derrota += 1
        elif pc == 2:
            print(f'{cor['green']}Jogador venceu')
            vitoria += 1
        elif pc == 3:
            print(f'{cor['purple']}EMPATE')
            empate += 1
    print(f'{cor['clean']}')
    
    while True:
        r = str(input('quer continuar a jogar? [S/N]')).strip().upper()
        if r:
            r = r[0]
            if r in 'SN':
                break
    if r == 'N':
        break
print('Programa encerrado')
print(f"""
{cor['green']}{vitoria} vitórias
{cor['red']}{derrota} derrotas
{cor['purple']}{empate} empates
""")