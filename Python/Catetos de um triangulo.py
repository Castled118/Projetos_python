from math import sqrt
C1=int(input('Qual é primeiro cateto do seu triângulo: '))
C2=int(input('E o segundo:'))
print('A hipotenusa de um triângulo retângulo de catetos {0} e {1} é igual a {2:.3f}!'.format(C1,C2,sqrt(C1**2+C2**2)))
