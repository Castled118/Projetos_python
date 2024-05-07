n1=int(input('Digite um número: '))
n2=int(input('Digite um número: '))
n3=int(input('Digite um número: '))
n4=int(input('Digite um número: '))
tupla=(n1,n2,n3,n4)
print(f'O número 9 aparece {tupla.count(9)} vezes,',end='')
if tupla.count(3)>0: 
    print(f' o número três tem sua primeira ocorrencia na posição {tupla .index(3)+1} e ', end='')
else:
    print('o número 3 não aparece e', end='')
s=0
for n in tupla:
    if n%2 == 0:
        s+=1
if s>0:
    print('os números', end=' ')
    for n in tupla:
        if n%2 == 0:
            print(f'{n}', end=' ')
    print('são pares!')
else:
    print('nenhum número é par!')