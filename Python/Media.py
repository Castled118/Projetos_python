n1= float(input('Digite sua nota na p1: '))
n2= float(input('Digite sua nota na p2: '))
media= (n1+n1)/2
cores = {'vermelho': '\033[4;31m', 'amarelo':'\033[4;33m', 'verde': '\033[4;32m', 'limpo':'\033[m'}
if media<5:
    print(f'Você foi {cores["vermelho"]}reprovado{cores["limpo"]} com uma média de {media}')
elif media>=5:
    print(f'Você foi {cores["verde"]}aprovado{cores["limpo"]} com uma média de {media}')
