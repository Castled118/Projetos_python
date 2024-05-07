n1=int(input('Em qual ano você nasceu: '))
n2=int(input('Em que ano estamos: '))
n3=n2-n1
if n3>18:
    print(f'Você ja excedeu a idade minima de alistamento em {n3-18} anos!')
elif n3<18:
    print(f'Ainda faltam {18-n3} anos para você se alistar!')
elif n3 == 18:
    print(f'Você está na idade certa para se alistar!')