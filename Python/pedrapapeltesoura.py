
from random import choice

# Lista de opções
opcoes = [1, 2, 3]

# Escolha aleatória da máquina
escolha_pc = choice(opcoes)
print(escolha_pc)

# Escolha do usuário
escolha_humano = int(input('(1)Pedra\n(2)Papel\n(3)Tesoura\n'))

# Verificação se a escolha do usuário está dentro do intervalo válido
if escolha_humano not in opcoes:
    print('\033[4;31mERROR\033[m')
else:
    # Lógica para determinar o vencedor
    if escolha_humano == escolha_pc:
        print('Empate!')
    elif (escolha_humano == 1 and escolha_pc == 3) or \
         (escolha_humano == 2 and escolha_pc == 1) or \
         (escolha_humano == 3 and escolha_pc == 2):
        print('Você venceu!')
    else:
        print('Você perdeu!')