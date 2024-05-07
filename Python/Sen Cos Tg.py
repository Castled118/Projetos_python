import math as m
a=int(input('Qual o ângulo: '))
cores = {'limpo':'\033[m',
        'vermelho':'\033[4;32m',
        'verde':'\033[4;31m',
        'amarelo':'\033[4;33m'}
print (f'O seno de {a} é igual a {cores['vermelho']}{m.sin(m.radians(a))}{cores["limpo"]} o cosseno de  {a} é igual a {cores["verde"]}{m.cos(m.radians(a))}{cores["limpo"]} e a tangente de  {a} é igual a {cores["amarelo"]}{m.tan(m.radians(a))}{cores["limpo"]}')
