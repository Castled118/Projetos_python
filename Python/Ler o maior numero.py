n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n1 > n2:
#Se n1 for maior que n2 quer dizer que o maior número e ou n1 ou n3, então checamos se n1 é maior que n3 na linha seguinte!
    if n1 > n3:
        #Após checar temos que n1>n2 e n1>n3, logo n1 é o maior número mas não sabemos qual o menor número!
        print(f'{n1} é o maior número!')
        if  n2 > n3:
             #Então se n2 for maior que n3 temos n1>n2>n3 logo n3 é o menor
             print(f'{n3} é o menor número!')
        else:
            #E caso contrário n2 é o menor número!
            print(f'{n2} é o menor número!')
    #E caso n1  não seja maior que n3 temos que n1>n2 e n3>n1(n3>n1>n2), então o maior É O n3 e o menor é o n2 
    else:
        print(f'{n3} é o maior número!')
        print(f'{n2} é o menor número!')
else:
    #Mas caso n1 não seja maior que n2 então os maiores são ou n2 ou n3, então checamos na linha seguinte!
    if n2 > n3:
    #E se isso for verdade n2 é o maior número (n2>n3 e n2>n1), mas não sabemos qual é o menor ainda!
        print(f'{n2} é o maior número!')
        #Então checamos qual é o menor na estrutura condicional a senguir!
        if n3 > n1:
            print(f'{n1} é o menor número!')
        else:
            print(f'{n3} é o menor número!')
    #Mas caso isso não seja verdade então n3 pe o maior pois n2 > n1 e n3 > n2, e com isso também concluimos que n1 é o menor número!
    else:
        print(f'{n3} é  o maior número!')
        print(f'{n1} é o menor número!')
#FORMA OTIMIZADA
menor = n1
maior = n1
if n2<n1 and n2<n3: #Checamos se n2 é o menor e caso seja apenas checamos qual é o maior, entre n3 e n1!
    menor = n2
    if n1 > n3:
        maior = n1
    else:
        maior = n3
elif n3<n1 and n3<n2: 
    menor=n3
    if n1 > n2:
        maior = n1
    else:
        maior = n2
elif n1 == menor:
    if n2 > n3:
        maior = n2
    else:
        maior = n3
print(f'{maior} é o maior número!')
print(f'{menor} é o menor número!')