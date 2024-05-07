lista=[]
#Perguntar a quantidade de itens:
quantidade=str(input('Quantos números você deseja inserir: '))
#Checar se a quantidade é um número válido
while not(quantidade.isnumeric()):
    quantidade=str(input('Insira um valor válido: '))
quantidade=int(quantidade)


#Perguntar os número e atribuilos a lista:
for n in range(0,quantidade):
    numero=str(input('Digite um número: '))
    while not(numero.isnumeric()):
        numero=str(input('Digite um número válido: '))
    numero=int(numero)
    lista.append(numero)


#Criar uma cópia da lista anterior para colocala em ordem crescente a ainda conseguir encontra o indice de um número
lista_certa=lista[:]
lista_certa.sort()


#Escrever os valores digitados
print('Os valors digitados foram:', end=' ')
for n in lista:
    print(n,end=' ')

#Escrever os número e seus indices para a lista correta:
for p,n in enumerate(lista_certa):
    #Para o sorted o maior indice é sempre o maior número e o menor é sempre o menor número:
    if p ==(len(lista_certa)-1):
        #Escrevemos o número e logo após o indice desse número na lista não 'sorted'
        print(f'O maior número foi o {n} na posição {lista.index(n)+1}')
    if p ==0:
        #Escrevemos o número e logo após o indice desse número na lista não 'sorted'
        print(f'\nO menor número foi o {n} na posição {lista.index(n)+1}')