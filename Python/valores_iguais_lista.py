resposta=''
lista=[]

#Em quanto a resposta para continuar for sim nos continuaremos
while resposta!='N':

    #No caso de checagem por laço nos atribuimos s=0 no começo de toda repetição
    s=0
    
    #Perguntar um número
    numero=str(input('Digite um número: '))
    #Checar se ele é valido
    while not(numero.isnumeric()):
        numero=str(input('Insira um valor válido: '))
    numero=int(numero)

    #Checar se ele ja está na lista
    if numero not in lista:
        lista.append(numero)
        print('Número adicionado com sucesso...')
    else:
        print('O número ja existe na lista, logo ele não será adicionado!')

    #Perguntar se ele deseja continuar
    resposta=str(input('Você deseja continuar? [S/N]')).upper().strip()
    #Checar se a resposta é valida
    while resposta not in 'SN':
        resposta=str(input('Insira um valor válido, você deseja continuar? [S/N] ')).upper().strip()


#Organizar a lista de forma crescente e escrever os valores digitados       
lista.sort()
print('Você digitou os valores: ',end='')
for n in lista:
    print(n,end=' ')


#Checar se o numero está na lista através de um laço!
    for n in lista:
        if numero == n:
            s+=1
    if s==0:
        lista.append(numero)
        print('Número adicionado com sucesso...')
    else:
        print('O número ja existe na lista, logo ele não será adicionado!')