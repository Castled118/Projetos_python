i = int(input('Qual a sua idade: '))
if i<= 9:
    print('Você pertence a categoria mirim!')
elif i<=14 and i>9:
    print('Você pertence a categoria infantil!')
elif i<=19 and i > 14:
    print('Você pertence a categoria junior!')
elif i<=20 and i > 19:
    print('Você pertence a categoria sênior!')
else:
    print('Você pertence a categoria master!')