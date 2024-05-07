media_alunos=[]
dados_total=[]
dados_nota=[]
dados_aluno=[]
resposta=''
notas=0
media=0

#Função criada para checar se a variavel i é numerica e caso contrario print j até que i seja númerico!
def checar_num(i, j):
    while not str(i).isnumeric():
        i = input(j)
    return (i)


#Pergunta duas notas, checa se elas são númericas e inseri elas em uma lista de notas
def colocar_nota():
    n1=str(input('Qual foi a primeira nota: '))
    n1=int(checar_num(n1,'Digite uma nota válida: '))
    n2=str(input('Qual foi a segunda nota do aluno: '))
    n2=int(checar_num(n2,'Digite uma nota válida: '))
    dados_nota.append(n1)
    dados_nota.append(n2)
    return


#Em quanto a resposta para se quer continuar for sim o loop continuara:
while resposta!='N':


    #Perguntar a quantidade de alunos que deseja cadastrar e checar se é númerico
    quantidade=str(input('Quantos alunos serão cadastrados: '))
    quantidade=int(checar_num(quantidade,'Digite um valor válido: '))


    #Loop para perguntar as informações baseadas no número de alunos
    for n in range(0,quantidade):


        #Perguntar o nome e inserir em uma sublista de dados de um aluno
        nome=str(input('Qual o nome do aluno: '))
        dados_aluno.append(nome)


        #Perguntar nota 
        colocar_nota()


        #Coloca a nota lista nota do aluno dentro da lista dado do aluno e após isso coloca a lista dado do aluno dentro da lista dados total
        dados_aluno.append(dados_nota[:])
        dados_total.append(dados_aluno[:])


        #Apaga a lista dado aluno e nota para um novo aluno ser cadastrado
        dados_aluno.clear()
        dados_nota.clear()


    #Pergunta se quer continuar e checa se a resposta é valida
    resposta=str(input('Você deseja continuar: [S/N] ').upper().strip())
    while resposta not in 'SN':
        resposta=str(input('Você deseja continuar: [S/N]').upper().strip())
print('-='*30)
print('No   Nome          Média')
print('-'*24)


#Escreve de forma formatada o nome número e média dos alunos
for i in range(0,len(dados_total)):
    media=(dados_total[i][1][0]+dados_total[i][1][1])/2
    print(i+1,end=' '*(5-len(str(i+1))))
    print(dados_total[i][0],end=' '*(19-len(dados_total[i][0])-(len(str(media)))))
    print(media)

opcao=''


#Cria uma lista ordenada pela média
for i in range(len(dados_total)):
    nome_aluno = dados_total[i][0]
    notas = dados_total[i][1]
    media = sum(notas) / len(notas)
    media_alunos.append([nome_aluno, media])
#lambda cria o criterio na qual a lista sera organizada, nesse caso o x[x][1], que é onde as médias estão armazenadas
media_alunos.sort(key=lambda x: x[1], reverse=True)

#Cria uma lista ordenada pelo nome
for i in range(len(dados_total)):
    nome_alunos=dados_total[:]
#Mesma coisa das médias porem x[x][0] é o local dos nomes
nome_alunos.sort(key=lambda x: x[0])


#Cria um loop em que caso a váriavel opcao seja o loop se quebra
while opcao!=4:

    #Pergunta e checa se a opção é válida
    opcao=str(input('''[1]Nota individual de aluno\n[2]Lista ordem por média\n[3]Lista ordem alfabética\n[4]Sair\n'''))
    opcao=int(checar_num(opcao,'Insira um valor válido\n[1]Nota individual de aluno\n[2]Lista ordem por média\n[3]Lista ordem alfabética\n[4]Sair\n'))

    #Se a opção for um ele roda o código para pergunta de notas individual
    if opcao==1:

        #Estrutura para saber as notas individualmente de cada aluno
        while True:
            

            #Perguntar sobre qual aluno e checar se a resposta é válida e se ela for 999 quebrar o loop
            aluno=str(input('Quer ver as notas de qual aluno(999 interrompe): '))
            aluno=int(checar_num(aluno,f'Digite um número válido (1,{len(dados_total)}): '))
            if aluno==999:
                break

            
            #Checar se a resposta esta válida em relação ao número de alunos
            while not(len(dados_total)-1>=aluno-1>=0):
                aluno=str(input(f'Digite um valor válido (1,{len(dados_total)}): ')).strip()
                aluno=int(checar_num(aluno,f'Digite um número válido (1,{len(dados_total)}): '))
                if aluno==999:
                    break

            #Escrever a nota e o nome do aluno
            aluno=int(aluno)
            if aluno==999:
                break
            print(f'As notas do aluno {dados_total[aluno-1][0]} foram igual a: {dados_total[aluno-1][1]}')
    

    #Se for 2 ele escreve a tabela por ordem de média
    if opcao==2:
        print('-='*30)
        print('No   Nome          Média')
        print('-'*24)
        for i in range(0,len(media_alunos)):
            print(i+1,end=' '*(5-len(str(i+1))))
            print(media_alunos[i][0],end=' '*(19-len(media_alunos[i][0])-(len(str(media_alunos[i][1])))))
            print(media_alunos[i][1])


    #Se for 3 escreve por ordem de nome
    if opcao==3:
        print('-='*30)
        print('No   Nome          Média')
        print('-'*24)
        for i in range(0,len(nome_alunos)):
            media=(nome_alunos[i][1][0]+nome_alunos[i][1][1])/2
            print(i+1,end=' '*(5-len(str(i+1))))
            print(nome_alunos[i][0],end=' '*(19-len(nome_alunos[i][0])-(len(str(media)))))
            print(media)
    

    #E 4 ele quebra o loop
    if opcao==4:
        break
