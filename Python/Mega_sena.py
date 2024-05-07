from random import randint
jogos=str(input('Quantos jogos serão jogados: ')).strip()
while not(jogos.isnumeric()):
    jogos=str(input('Insira uma resposta válida, quantos jogos serão jogados: '))
jogos=int(jogos)
total=[]
parcial=[]
for i in range (0,jogos):
    for k in range(0,6):
        parcial.append(randint(1,60))
    total.append(parcial[:])
    parcial.clear()
print('Os sorteios seraõ: ')
for l in range(0,jogos):
    for y in total[l]:
        y=str(y)
        print(y,end='-'*(3-len(y)))     
    print()


