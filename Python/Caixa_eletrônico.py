sacar=int(input('Quantos reais você deseja sacar: '))
cedula_50=0
cedula_20=0
cedula_10=0
cedula_1=0
while True:
    if sacar>=50:
        cedula_50+=1
        sacar-=50
    elif sacar>=20:
        sacar>=20
        cedula_20+=1
        sacar-=20
    elif sacar>=10:
        cedula_10+=1
        sacar-=10
    elif sacar>=1:
        cedula_1+=1
        sacar-=1
    if sacar == 0:
        break
print(f'Você receberá {cedula_50} cédulas de 50R$, {cedula_20} de 20R$, {cedula_10} de 10R$ e {cedula_1} de 1R$')
