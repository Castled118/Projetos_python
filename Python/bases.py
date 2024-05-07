import math as mt
numero = int(input('Digite um número: '))
base = (str(input('(1)binário, (2)octal, (3)hexadecimal: ')))
if base.isnumeric():
    if base.count('1')>base.count('2') and base.count('1')>base.count('3'):
        base = 1
    elif base.count('2')>base.count('3') and base.count('2')>base.count('1'):
        base = 2
    elif base.count('3')>base.count('2') and base.count('3')>base.count('1'):
        base = 3
elif base.isalpha() or base.isalnum():
    print('\033[4;31mERROR\033[m')
    base = 4
if base == 1:
    print(f'O número {numero} em binário é igual a {bin(numero)}')
elif base == 2:
    print(f'O número {numero} em octal é igual a {oct(numero)}')
elif base == 3:
    print(f'O número {numero} em hexadecimal é igual a {hex(numero)}')
