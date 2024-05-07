s1=float(input('Qual o seu salário: '))
if s1 > 1250:
    s2 = s1+(s1*1/10)
else:
    s2 = s1+(s1*15/100)
print(f'O salário de {s1} passa a ser {s2:.2f}')
