import pandas as pd
import os
import PySimpleGUI as pg
media_alunos=[]
dados_total=[]
dados_nota=[]
dados_aluno=[]
resposta=''
notas=0
media=0
pg.theme('Dark')
#Função criada para checar se a variavel i é numerica e caso contrario print j até que i seja númerico!
def checar_num(i, j):
    while not str(i).isnumeric():
        i = input(j)
    return (i)


#Pergunta se ele quer modificar uma planilha excel e checa se a resposta é válida:
layout1=[[pg.Text('Você deseja acresentar valores a uma planilha excel: [S/N] ')],[pg.Button('Sim'),pg.Button('Não')]]
janela1=pg.Window('Opção excel',layout1)
while True:
    #Checar os valores dos botões
    event1,value1=janela1.read()
    if event1==pg.WINDOW_CLOSED:
        break
    elif event1=='Sim':
        desejo='S'
        break
    elif event1=='Não':
        desejo='N'
        break
janela1.close()



#Checa se a resposta é sim
if desejo=='S':
    #Lista auxiliar é criadas
    lista_x=[]

    # Pergunta o caminho da planilha e checa se ele é válido, com interface
    layout2=[pg.Text(('Qual o caminho da planilha criada por esse algoritmo: ').strip()),pg.Input(key='-FILE-'),pg.FileBrowse()],[pg.Button('OK')]
    janela2=pg.Window('Caminho',layout2)
    while True:
        event2,value2=janela2.read()
        if event2==pg.WIN_CLOSED:
            break
        #Se o botão ok for clicado checamos se a variavel e um arquivo e se ele termina com .xlsx
        elif event2=='OK' or event2=='\r':
            caminho_planilha = value2['-FILE-']
            if os.path.isfile(caminho_planilha) and caminho_planilha.lower().endswith('.xlsx'):
                break
            else:
                pg.popup_error('Insira um caminho válido para um arquivo .xlsx')
    janela2.close()



    #Cria duas listas, uma com nome e outra com notas
    planilha_notas=pd.read_excel(caminho_planilha,usecols=[2])
    planilha_nomes=pd.read_excel(caminho_planilha,usecols=[1])


    #Para o número de nomes fazemos o seguinte procedimento
    for i in range(0,len(planilha_nomes)):
       

       #Incluimos o nome na sub-lista
       lista_x.append(planilha_nomes['Nome'].iloc[i])
       
       #Transformamos a string '[]' em []
       k=eval(planilha_notas['Notas'].iloc[i])

       #Inserirmos os valores a lista original
       lista_x.append(k)
       dados_total.append(lista_x[:])
       lista_x.clear()
        
    
#Perguntamos quantas notas serão inseridas
layout3=[pg.Text('Quantas notas serão inseridas: '),pg.Input(key='NOTA')],[pg.Button('Confirmar')]
janela3=pg.Window('NOTAS',layout3)
while True:
    event3,value3=janela3.read()
    if event3==pg.WIN_CLOSED:
        break
    elif event3=='Confirmar':
        notas=value3['NOTA']
        #Se o valor não for númerico ele escreva isso:
        if not(notas.isnumeric()):
            pg.popup_error('Insira um valor válido: ') 
        #E se for a página se fecha para e continuamos o código     
        elif notas.isnumeric():
            notas=int(notas)
            break
janela3.close()


#Pergunta x notas, checa se elas são númericas e inseri elas em uma lista de notas
def colocar_nota():
    notas_temporarias=[]
    #Criamos o layout com base no número de notas que o usuario pediu
    layout5=[[[pg.Text('Digite o nome: '),pg.Input(tooltip='Nome',key='NOME')]],[pg.Text('Digite as notas: ')],]
    #Para cada nota criamos um bloco input para o layout 
    for i in range(0,notas):
        layout5.append([pg.Input(tooltip='Nota',key=f'NOTA{i}')],)
    
    layout5.append([pg.Button('Confirmar')])
    janela5=pg.Window('Notas', layout5 )
    while True:
        event5,value5=janela5.read()
        if event5==pg.WIN_CLOSED:
            break
        #Se o botão confirmar for clicado executamos diversos procedimentos
        elif event5 == 'Confirmar':
            
            #Atribuimos o nome a lista 'Dados do aluno'
            nome=''
            nome=value5['NOME']
            dados_aluno.append(nome[:]) # Inseri o nome ao dados do aluno

            #Limpamos a notas temporarias e criamos uma variavel auxiliar para nos ajudar a checar nota
            notas_temporarias.clear()
            notas_validas = True 
            for i in range(notas):
                while True:
                    n1 = value5[f'NOTA{i}'].strip()
                    #Se a nota for númerica a string é convertida em float
                    if n1.replace('.', '', 1).isnumeric():
                        n1 = float(n1)
                        #Se a nota for válida atribuimos ela a notas temporarias
                        if 1 <= n1 <= 10:
                            notas_temporarias.append(n1)
                            break
                        else:
                            #Atribuimos a variavel com False, isso impede que se tivermos 2 notas, 1 certa e a outra errada, a certa seja adicionada e quando a errada se tornar 
                            #certa tenhamos 2 notas iguais, que foi a nota que sempre esteve certa
                            # Se uma nota não for válida, altera a variável para False
                            notas_validas = False  
                            pg.popup_error(f'As nota {i+1} devem ser entre 1 e 10.')
                            # Sai do loop interno se a nota for inválida
                            break  
                    else:

                        pg.popup_error(f'A nota {i+1} não é númerica!')
                        #Atribuimos a variavel com False, isso impede que se tivermos 2 notas, 1 certa e a outra errada, a certa seja adicionada e quando a errada se tornar 
                        #certa tenhamos 2 notas iguais, que foi a nota que sempre esteve certa
                        # Se uma nota não for válida, altera a variável para False
                        notas_validas = False  
                        break  # Sai do loop interno se a nota não for numérica
            #Se todas as notas forem válidas simultaneamente
            if notas_validas:
                #Botamos as notas no dados do aluno, então teremos uma lista com nome e dentro dessa lista uma lista com notas.
                dados_aluno.append(notas_temporarias[:])
                #Atribuimos os dados a lista total
                dados_total.append(dados_aluno[:])
                #limpas as lista intermediarias para os próximos alunos
                dados_nota.clear()
                dados_aluno.clear()
                break  # Sai do loop principal se todas as notas forem válidas
    janela5.close()


#Em quanto a resposta para se quer continuar for sim o loop continuara:
while resposta!='N':


    #Perguntar a quantidade de alunos que deseja cadastrar e checar se é númerico
    #Criação de layout
    layout4=[pg.Text('Quantos alunos serão cadastrados: '),pg.Input(key='ALUNOS')],[pg.Button('Confirmar')]
    janela4=pg.Window('Quantidade Alunos',layout4)
    while True:
        event4,value4=janela4.read()
        if event4==pg.WIN_CLOSED:
            break
        elif event4=='Confirmar' or event4=='\r':
            quantidade=value4['ALUNOS']
            if not(quantidade.isnumeric()):
                pg.popup_error('Insira um valor válido')
            elif quantidade.isnumeric():
                quantidade=int(quantidade)
                break
    janela4.close()
    #Loop para perguntar as informações baseadas no número de alunos
    for n in range(quantidade):
        #Perguntar nota, nome e inserila em uma lista com os dados totais.
        colocar_nota()



    #Pergunta se quer continuar e checa se a resposta é valida
    layout6=[pg.Text('Você deseja inserir mais alunos: ')],[pg.Button('Sim')],[pg.Button('Não')]
    janela6=pg.Window('Continuar', layout6)
    while True:
        event5,value5=janela6.read()
        if event5==pg.WIN_CLOSED:
            break
        elif event5=='Sim':
            resposta='S'
            break
        elif event5=='Não':
            resposta='N'
            break
    janela6.close()
opcao=''
#Cria uma lista ordenada pela média
for i in range(len(dados_total)):
    nome_aluno = dados_total[i][0]
    nota = dados_total[i][1]
    media1 = sum(nota) / len(nota)
    media_alunos.append([nome_aluno, f'{media1:.2f}'])
#lambda cria o criterio na qual a lista sera organizada, nesse caso o x[x][1], que é onde as médias estão armazenadas
media_alunos.sort(key=lambda x: x[1], reverse=True)

#Cria uma lista ordenada pelo nome
for i in range(len(dados_total)):
    nome_alunos=dados_total[:]
#Mesma coisa das médias porem x[x][0] é o local dos nomes
nome_alunos.sort(key=lambda x: x[0])


#Cria um loop em que caso a váriavel opcao seja o loop se quebra
while opcao!=4:


    #Escreve de forma formatada o nome número e média dos alunos e inseri no layout
    layout7=[[pg.Text('No', size=(5, 1)), pg.Text('Nome', size=(20, 1)), pg.Text('Média', size=(10, 1))],]
    #Para cada aluno adicionamos ele no layout
    for i in range(len(dados_total)):
        nome = dados_total[i][0]
        nota = dados_total[i][1]
        media2 = sum(nota) / len(nota)
        #Após atribuirmos variaves intermediarias colocamos o indice+1, para ser o número do aluno, o nome, e por último a media
        layout7.append([
        pg.Text(str(i+1), size=(5, 1)),
        pg.Text(nome, size=(20, 1)),
        pg.Text(f'{media2:.1f}', size=(10, 1)),
        ])
    #Também incluimos botões para diferentes funçoes e checamos se foram clicados
    layout7.append([pg.Button('Nota individual de aluno'),pg.Button('Lista ordem por média'),pg.Button('Lista ordem alfabética'),pg.Button('Sair')])
    janela7=pg.Window('Médias',layout7)
    while True:
        event7, value7 = janela7.read()
        if event7 == pg.WINDOW_CLOSED:
            break
        elif event7=='Nota individual de aluno':
            opcao=1
            break
        elif event7=='Lista ordem por média':
            opcao=2
            break
        elif event7=='Lista ordem alfabética':
            opcao=3
            break
        elif event7=='Sair':
            opcao=4
            break
    janela7.close()


    #Se a opção for um ele roda o código para pergunta de notas individual
    if opcao==1:
        #Reescrever a lista novamente por fins de consulta
        layout8 = [
            [pg.Text('No', size=(5, 1)), pg.Text('Nome', size=(20, 1)), pg.Text('Média', size=(10, 1))]
        ]
        for aluno in (dados_total):
            nome = aluno[0]
            nota = aluno[1]
            media3 = sum(nota) / len(nota)
            layout8.append([
                pg.Text(str(dados_total.index(aluno)+1), size=(5, 1)), 
                pg.Text(nome, size=(20, 1)), 
                pg.Text(f'{media3:.1f}', size=(10, 1))
            ])
        layout8.append([pg.Button('Continuar')])
        janela8 = pg.Window('Dados dos Alunos', layout8)
        while True:
            event8, values8 = janela8.read()
            if event8 == pg.WINDOW_CLOSED or event8=='Continuar':
                break


        #Estrutura para saber as notas individualmente de cada aluno
        while True:
            
            layout9=[pg.Text('Quer ver as notas de qual aluno: '),pg.Input(tooltip='Número na lista',key='NOTA_ALUNO')],[pg.Button('Pesquisar'),pg.Button('Sair')]
            janela9=pg.Window('Notas',layout9)
            aluno_valido=True
            while True:
                event9, value9=janela9.read()
                if event9==pg.WIN_CLOSED or event9=='Sair':
                    break
                #Se o botão pesquisar for clicado checamos diversas coisas
                elif event9=='Pesquisar':
                    aluno=str(value9['NOTA_ALUNO'])
                    aluno_valido=True # variavel auxiliar
                    #Se o número do aluno for númerico transformamos ele em um valor inteiro
                    if aluno.isnumeric():
                        aluno=int(aluno)
                        #Agora checamos se o aluno está dentro dos indices, ou seja, se ele esta incluido na lista
                        if len(dados_total)>=aluno>=1:
                            print(f'As notas do aluno {dados_total[aluno-1][0]} foram igual a: {dados_total[aluno-1][1]}')
                        #Caso contrário atribuimos a variavel a False e escrevemos um erro
                        else:                                            
                            pg.popup_error(f'Digite um aluno válido entre 1,{len(dados_total)}')
                            aluno_valido=False   
                    #Caso o número não seja númerico, escrevemos um erro e atribuimos a auxiliar para falso, logo as notas não serão imprimidas                                    
                    else:
                        pg.popup_error(f'Digite um valor númerico!')
                        aluno_valido=False 
                #Caso a variavel seja True, ou seja, o valor é valido escrevemos:     
                if aluno_valido:
                    #Checamos se o valor na lista original não for sair, que caso sim ele não imprimira as notas
                    if  event9==pg.WIN_CLOSED or event9=='Sair':
                        break
                    else:
                        #Criamos um layout com nota e nome
                        layout10=[[pg.Text(f'As notas do aluno {dados_total[aluno-1][0]} foram igual a: {dados_total[aluno-1][1]}')],[pg.Button('Fechar')]]
                        janela10=pg.Window('Notas',layout10)
                        #Imprimimos o layotu
                        while True:
                            event10,value10=janela10.read()
                            if event10==pg.WIN_CLOSED or event10=='Fechar':
                                break
                        #fechamos as notas
                        janela10.close()
            #Se o botao sair for clicado, o loop é quebrado e fechamos todas as janelas juntamente do loop que deixam elas ligadas
            janela9.close()
            janela8.close()
            break


    #Se for 2 ele escreve a tabela por ordem de média
    if opcao==2:
        #Mesma formatação da primeira impressão mas com a lista de organizada por médias
        layout11=[[pg.Text('No', size=(5, 1)), pg.Text('Nome', size=(20, 1)), pg.Text('Média', size=(10, 1))]]
        for aluno in (media_alunos):
            nome = aluno[0]
            media4 = aluno[1]
            media4=float(media4)
            layout11.append([
                pg.Text(str(media_alunos.index(aluno)+1), size=(5, 1)), 
                pg.Text(nome, size=(20, 1)), 
                pg.Text(f'{media4:.1f}', size=(10, 1))
            ])
        layout11.append([pg.Button('Nota individual de aluno'),pg.Button('Lista ordem por média'),pg.Button('Lista ordem alfabética'),pg.Button('Sair')])
        janela11=pg.Window('Médias',layout11)
        while True:
            event11, value11 = janela11.read()
            if event11 == pg.WINDOW_CLOSED:
                break
            elif event11=='Nota individual de aluno':
                opcao=1
                break
            elif event11=='Lista ordem por média':
                opcao=2
                break
            elif event11=='Lista ordem alfabética':
                opcao=3
                break
            elif event11=='Sair':
                opcao=4
                break
        janela11.close()


    #Se for opcao for 3 escreve por ordem de nome
    if opcao==3:
        #Mesma formatação da primeira impressão mas com a lista de organizada por médias
        layout12=[[pg.Text('No', size=(5, 1)), pg.Text('Nome', size=(20, 1)), pg.Text('Média', size=(10, 1))]]
        for aluno in (nome_alunos):
            nome = aluno[0]
            nota = aluno[1]
            media5 = sum(nota)/len(nota)
            layout12.append([
                pg.Text(str(nome_alunos.index(aluno)+1), size=(5, 1)), 
                pg.Text(nome, size=(20, 1)), 
                pg.Text(f'{media5:.1f}', size=(10, 1))
            ])
        layout12.append([pg.Button('Nota individual de aluno'),pg.Button('Lista ordem por média'),pg.Button('Lista ordem alfabética'),pg.Button('Sair')])
        janela12=pg.Window('Médias',layout12)
        while True:
            event12, value12 = janela12.read()
            if event12 == pg.WINDOW_CLOSED:
                break
            elif event12=='Nota individual de aluno':
                opcao=1
                break
            elif event12=='Lista ordem por média':
                opcao=2
                break
            elif event12=='Lista ordem alfabética':
                opcao=3
                break
            elif event12=='Sair':
                opcao=4
                break
        janela12.close()


    #E 4 ele quebra o loop
    if opcao==4:
        break

#variaveis auxiliares
ops=''
ops1=''


#Criação do dataframe , em que declaramos o nome das colunas e falamos os dados da coluna
tabela=pd.DataFrame({'Nome':[dados_total[i][0]for i in range(0,len(dados_total))],
                     'Notas':[dados_total[i][1]for i in range(0,len(dados_total))],
                     'Ordem alfabética->':ops,
                     'Nomes1':[nome_alunos[i][0]for i in range(0,len(nome_alunos))],
                     'Nota1':[nome_alunos[i][1]for i in range(0,len(nome_alunos))],
                     'Ordem de média->':ops1,
                     'Nomes2':[media_alunos[i][0]for i in range(0,len(media_alunos))],
                     'Média':[media_alunos[i][1]for i in range(0,len(media_alunos))]})


#Criação da planilha excel
#Pergunta do nome
layout13=[[pg.Text('Qual será o nome desse arquivo: '),pg.Input(key='NOME_ARQ')],[pg.Button('OK')]]
janela13=pg.Window('ARQUIVO',layout13)
while True:
    event13,value13=janela13.read()
    nome_tabela=value13['NOME_ARQ']
    if event13==pg.WIN_CLOSED or event13=='OK':
        break
janela13.close()
tabela.to_excel(f'{nome_tabela}.xlsx')
