import PySimpleGUI as sg
dados_total=[['a', [5, 3, 7]], ['b', [6, 4, 2]], ['c', [8, 4, 8]], ['a', [5, 2, 6]], ['b', [4, 2, 7]], ['matheus', [4, 6]], ['jao', [6, 3]], ['luana', [3, 9]], ['augusto', [56, 7]], ['pedro', [2, 7]], ['LUANA', [1, 7]], ['matheus', [4, 5]], ['joao', [2, 5]], ['luana', [2, 3]], ['caii', [3, 1]], ['matheus', [3.0, 4.0]], ['joao', [5.0, 4.0]]]
def calcular_media(notas):
    return sum(notas) / len(notas)

# Layout da janela principal
layout = [
    [sg.Text('No', size=(5, 1)), sg.Text('Nome', size=(20, 1)), sg.Text('Média', size=(10, 1))]
]

# Adiciona cada aluno ao layout
for i, aluno in enumerate(dados_total):
    nome = aluno[0]
    notas = aluno[1]
    media = calcular_media(notas)
    layout.append([
        sg.Text(str(i+1), size=(5, 1)), 
        sg.Text(nome, size=(20, 1)), 
        sg.Text(f'{media:.1f}', size=(10, 1))
    ])

# Cria a janela
window = sg.Window('Dados dos Alunos', layout)

# Loop para eventos da janela
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

# Fecha a janela ao finalizar
window.close()