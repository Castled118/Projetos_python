lista=[]
resposta=''
algarismos=0
while resposta!='N':
    numero=str(input('Digite um número: '))
    while not(numero.isnumeric()):
        numero=str(input('Insira um valor válido: '))
    algarismos+=len(numero)
    numero=int(numero) 
    lista.append(numero) 
    resposta=str(input('Você deseja continuar? [S/N]')).upper().strip()
    while resposta not in 'SN':
        resposta=str(input('Insira um valor válido, você deseja continuar? [S/N] ')).upper().strip()
print('=-'*60)
print(f'Você digitou {algarismos} algarismos!')
if lista.count(5)>=1:
    print('O número 5 aparece nas posições: ',end='')
    for k in range (0,len(lista)):
        if lista[k]==5:
            print(k+1,end=' ')
else:
    print('\nO 5 não faz parte da lista!')

lista.sort(reverse=True)
print(f'\nOs valores em ordem decrescente são: ', end='')
for num in lista:
    print(num,end=' ')