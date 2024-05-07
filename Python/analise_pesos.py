#Declaração variáveis
resposta=''
pessoas=[]
pessoas_cadastradas=0
maior_peso=0
menor_peso=0
pessoas_maior_peso=[]
pessoas_menor_peso=[]

#Corpo do código, em que cada vez ele checa se a condição de continuar é um N, pois se for devemos parar!
while resposta!='N':

    #Perguntar o nome
    nome=str(input('Digite o seu nome: '))

    #Perguntar o peso e checar se ele é númerico
    peso=str(input('Digite seu peso: ')).strip()
    while not(peso.isnumeric()):
        peso=str(input('Digite um peso válido: ')).strip()
    peso=int(peso)

    #Perguntar se ele deseja continuar e checar se é uma resposta válida
    resposta=str(input('Você deseja continuar? [S/N] ')).upper().strip()
    while resposta not in 'SN':
        resposta=str(input('Digite uma resposta válida: [S/N] ')).upper().strip()
    
    #Checar se o peso dessa pessoa é o maior/menor/o primeiro
    if peso>maior_peso:
         maior_peso=peso
    if menor_peso==0:
         menor_peso=peso
    elif menor_peso>peso:
        menor_peso=peso

    #Atribuir o nome dessa pessoa a uma sublista, inserir a sublista na lista principal, e apagar as informações da sublista
    pessoa=[nome,peso]
    pessoas.append(pessoa[:])
    pessoa.clear()

    #Adicionar mais uma pessoa cadastrada
    pessoas_cadastradas+=1

#Escrever o número de pessoas cadastradas
print(f'{pessoas_cadastradas} pessoas foram cadastradas!')

#Checar as informações de peso para cada indice da lista principal
for n in range(0,pessoas_cadastradas):
        #Se o peso da pessoa for igual ao maior peso ela sera inserida na lista de pessoas com maior peso
        if pessoas[n][1]==maior_peso:
             pessoas_maior_peso.append(pessoas[n][0])
        #Caso ela não seja com maior peso, fazemos o mesmo processo mas para menor peso
        elif pessoas[n][1]==menor_peso:
             pessoas_menor_peso.append(pessoas[n][0])

#Escrevemos as pessoas com maior e menor peso de forma minimamente formatada
print(f'As pessoas com mais peso, {maior_peso}KG, foram ',end='')
for j in pessoas_maior_peso:
     print(j,end='  ')
print(f'\nAs pessoas com menor peso, {menor_peso}Kg, foram ',end='')
for i in pessoas_menor_peso:
     print(i,end=' ')