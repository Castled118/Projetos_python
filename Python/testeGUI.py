import PySimpleGUI as pg
def checar_num(i, j):
    while not str(i).isnumeric():
        i = input(j)
    return (i)
notas=3
dados_nota=[]
def colocar_nota():
    y=[]
    layout5=[pg.Text('Digite o nome e as notas: ')]
    for i in range(0,notas):
        layout5+=[pg.Input(key=(f'NOTA{i}'))]
        i
    layout5+=[pg.Button('Confirmar')]
    print(layout5)
    janela5=pg.Window('Notas', layout5 )
    while True:
        event5,value5=janela5.read()
        if event5==pg.WIN_CLOSED:
            break
        elif event5=='Confirmar':
            for i in range(0,notas):
                n1=value5[f'NOTA{i}']
                dados_nota.append(n1)
                y=+[value5[f'NOTA{i}']]

    for k in range(0,notas):

        n1=str(input(f'Qual foi a {k+1}º nota: '))
        n1=int(checar_num(n1,'Digite uma nota válida: '))
        while not(10>=n1>=0):
            n1=str(input('Digite uma nota válida: '))
            n1=int(checar_num(n1,'Digite uma nota válida: '))
        dados_nota.append(n1)
    return

colocar_nota()