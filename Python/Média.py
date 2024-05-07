
sum_=0
k=2
r=''
maior = menor = 0
n1=int(input('Digite um número: '))
n2=int(input('Digite um número: '))
if n1>n2:
    maior = n1
    menor = n2
elif n2>n1:
    maior = n2
    menor = n1
while r!='N':
    r=str(input('Você quer continuar: [S/N]')).upper()
    sum_+=n1
    if r=='S':
        n1=int(input('Digite um número: '))
        k+=1
    elif r=='N':
        print(f'A média foi de {(sum_+n2)/k}')
    else:
        print('Por favor insira uma resposta válida!')
    if n1> maior:
        maior = n1
    if n1<menor:
        menor = n1
print(f'O menor número foi o {menor} e o maior foi o {maior}')
