import platform
cord = ['']
for c in range (0,82):
    cord.append('□')
print('SUDOKU')
while True:
    print(f"""
      1  2  3  4  5  6  7  8  9 -> X
    1 {cord[1]}  {cord[2]}  {cord[3]}  {cord[4]}  {cord[5]}  {cord[6]}  {cord[7]}  {cord[8]}  {cord[9]}  
    2 {cord[10]}  {cord[11]}  {cord[12]}  {cord[13]}  {cord[14]}  {cord[15]}  {cord[16]}  {cord[17]}  {cord[18]}   
    3 {cord[19]}  {cord[20]}  {cord[21]}  {cord[22]}  {cord[23]}  {cord[24]}  {cord[25]}  {cord[26]}  {cord[27]}   
    4 {cord[28]}  {cord[29]}  {cord[30]}  {cord[31]}  {cord[32]}  {cord[33]}  {cord[34]}  {cord[35]}  {cord[36]}   
    5 {cord[37]}  {cord[38]}  {cord[39]}  {cord[40]}  {cord[41]}  {cord[42]}  {cord[43]}  {cord[44]}  {cord[45]}   
    6 {cord[46]}  {cord[47]}  {cord[48]}  {cord[49]}  {cord[50]}  {cord[51]}  {cord[52]}  {cord[53]}  {cord[54]}   
    7 {cord[55]}  {cord[56]}  {cord[57]}  {cord[58]}  {cord[59]}  {cord[60]}  {cord[61]}  {cord[62]}  {cord[63]}   
    8 {cord[64]}  {cord[65]}  {cord[66]}  {cord[67]}  {cord[68]}  {cord[69]}  {cord[70]}  {cord[71]}  {cord[72]}   
    9 {cord[73]}  {cord[74]}  {cord[75]}  {cord[76]}  {cord[77]}  {cord[78]}  {cord[79]}  {cord[80]}  {cord[81]}    
    |
    v
    Y 
    """)
    while True:
        while True:
            numero = str(input('Digite o número: '))
            cord_x = str(input('Digite a cordenada X: '))
            cord_y = str(input('Digite a cordenada Y: '))
            if numero.isnumeric() and cord_x.isnumeric() and cord_y.isnumeric():
                numero = int(numero)
                cord_x = int(cord_x)
                cord_y = int(cord_y)
                break
            else:
                print('digite entradas validas')

        if numero > 9:
            print('Digite um número válido')
        if cord_x <= 9 and cord_y <= 9:
            break
    i = int(input('num teste: '))
