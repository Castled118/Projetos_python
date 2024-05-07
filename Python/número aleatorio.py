import random as rd
import math as mt
n1= int(input('Tente adivinhar um núemro inteiro entre 1 e 100: '))
s1=mt.ceil((rd.uniform(1 , 100)))
if n1 == s1:
    print(f'Parabéns você acertou!\n O número realmente era {n1}')
else:
    print(f'Você errou, o número era {s1} e você colocou {n1}! :(')