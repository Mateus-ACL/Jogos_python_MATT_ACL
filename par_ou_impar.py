from random import randint
cor = {'clean':'\033[m',
         'yellow':'\033[33m',
         'green':'\033[1;32m',
         'purple':'\033[1;35m',
         'red':'\033[1;31m'}
imppar = ["ímpar","par"]
resultado = ["PERDEU","VENCEU"]
sequencia = 0

print(f'{cor['yellow']}⊞'*20)
print('JOGO DE ÍMPAR OU PAR')
print('⊞'*20,f'{cor['clean']}')

while True:
    while True:
        num = input('Digite um valor: ')
        if num.isnumeric():
            num = int(num)
            break
    while True:
        print(f'Par ou Ímpar? {cor['red']}[P/I]{cor['clean']}: ',end='')
        pi = str(input('')).upper().strip()[0]
        if pi in 'PI':
            break
    maq_num = randint(1,10)
    soma = num + maq_num
    calc = soma % 2
    mensg_1 = mensg_2 = 0
    if calc == 0:
        mensg_1 += 1

    if 'P' in pi and calc == 0:
        mensg_2 += 1
    elif 'I' in pi and calc != 0:
        mensg_2 += 1
    print(f'Você jogou {num} e o computador {maq_num}. Total de {soma}... deu {imppar[mensg_1]}')
    
    if mensg_2 == 0:
        cor_resultado = cor['red']
    else:
        cor_resultado = cor['green']

    print(cor_resultado+'⊞'*20)      
    print(f'Você {resultado[mensg_2]}')
    print('⊞'*20,cor['clean'])
    if mensg_2 == 0:
        break
    sequencia += 1
print(f'Sua sequência de vitória foi: {cor['purple']}{sequencia}')