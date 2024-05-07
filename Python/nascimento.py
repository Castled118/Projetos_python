from datetime import date
atual= date.today().year
n=0
s=0
for c in range(0,7):
    n1=int(input('Qual ano você nasceu: '))
    idade = atual -n1
    if idade>=18:
        s+=1
    else:
        n+=1
print(f'{s} pessoas são maiores de idade e {n} são menores!')