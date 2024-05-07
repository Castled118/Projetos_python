import random as rd
a1=str(input('Qual o nome do primeiro aluno: '))
a2=str(input('Qual o nome do segundo aluno: '))
a3=str(input('Qual o nome do terceiro aluno: '))
a4=str(input('Qual o nome do quarto aluno: '))
lista=[a1, a2, a3, a4]
print(f'O aluno escolhido foi: {rd.choice(lista)}')
rd.shuffle(lista)
print(f'E a ordem de apresentação sera{lista}')
