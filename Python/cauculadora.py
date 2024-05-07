n=0
a1=float(input('Digite um número: '))
a2=float(input('Digite um número: '))
while n!=5:
    n=int(input(f'Qual operação você deseja realizar: \n {'-'*12}\n[1]somar\n[2]multiplicar\n[3]maior\n[4]digitar novos números\n[5]sair do programa\n'))
    if n==1:
        print(f'A soma é igual a {a1+a2}')
    elif n==2:
        print(f'A multiplicação é igual a {a1*a2}')
    elif n==3:
        if a1>a2:
            print(f'{a1} é o maior número')
        else:
            print(f'{a2} é o maior número')
    elif n ==4:
        a1=float(input('Digite um número: '))
        a2=float(input('Digite um número: '))
    elif n == 5:
        n=5
    else:
        print('\033[4;31mERROR\033[m')
print('FIM')

    

