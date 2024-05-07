#Declarando variaveis
soma=0 
homem_velho=0
n4=0
numero_mulher=0
for c in range (0,4):
    #Perguntas
    n1=str(input('Qual o seu nome: '))
    n2=int(input('Qual a sua idade: '))
    n3= int(input('(1)Masculino; (2)Feminino: '))

    #Checar se n3 foi colocado corretamente:
    if n3 != 1 and n3 != 2:
        print('\033[4;31mERROR\033[m')
    soma+=n2

    #Checagem se os últimos inputs foram do homem mais velho:
    if n3 == 1 and n2 > homem_velho:
        homem_velho=n2
        nome_velho=n1
    
    #Checagem para ver quantas mulheres haviam:
    if n3 == 2:
        n4+=2

    #Checagem para ver se a mulher tem menos que 20 anos:
    if n3 == 2 and n2<20:
        numero_mulher+=1
#Checagem se todos os input foram mulheres, que caso verdadeiro não haviam homens , logo não haviam homens mais velhos:
if n4 == 8:
    nome_velho=('Não havia nenhum homem!')

#Respostas
print(f'{numero_mulher} mulheres tem menos que 20 anos!')
print(f'{nome_velho} é o homem mais velho!')
print(f'{soma/4} é a média das idades!')