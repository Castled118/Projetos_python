from random import randint
print('-='*11)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-='*11)
n3=''
s=0
while True:
    n3=''
    n1=int(input('Digite um número: '))
    n2= randint(1,10)
    while n3!='P' and n3!='I':
        n3=str(input('Par ou ímpar: [P/I] ')).upper()
        if n3!='P' and n3!='I':
            print('Insira um valor válido!')
    sum=n1+n2
    if sum%2==0:
        resultado='P'
    else:
        resultado='I'
    print(f'O computador colocou {n2} e você {n1}, logo,', end='')
    if resultado==n3:
        print(' você \033[4;32mvenceu!\033[m')
        s+=1
    elif resultado!=n3:
        print(' você \033[4;31mperdeu!\033[m')
        if s>0:
            if s==1:
                print('Você ganhou 1 vez!')
            else:
                print(f'Você ganhou {s} vezes antes de perder!')
        break