matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma_pares=0
soma_3coluna=0
maior_valor2linha=0
for n in range(0,3):
    for k in range(0,3):
       #Checar se valor é válido!
        valor=str(input(f'Digite um valor para a coordenada [{n},{k}]: '))
        while not(valor.isnumeric()):
            valor=str(input('Digite um valor válido: '))
        valor=int(valor)

        #Somar os pares
        if valor%2==0:
            soma_pares+=valor

        #Inseri-lo na cooredenada correta da matriz
        #Para esse modo de inserir o valor o indice ja deve existir, pois ele não sera criado apenas substituido
        matriz[n][k]=valor
        #Se quisermos criar um novo indice e inserir o valor escrevemos:
        #matriz[n].insert(k,valor)
        #E declaramos a matriz da seguinte forma:
        #matriz=[[],[],[]]

#printalo na tela
for j in range(0,len(matriz)):
    print()
    for y in matriz[j]:
        print(f'[{y: ^5}]',end='')
print()
print('-='*15)
print(f'A soma de todos os valores pares foi: {soma_pares}')
for y in range(0,len(matriz)):
    soma_3coluna+=matriz[y][2]
print(f'A soma de todos os valores da terceira coluna foi: {soma_3coluna}')
for m in range(0,len(matriz[1])):
    if maior_valor2linha==0:
        maior_valor2linha=matriz[1][m]
    elif maior_valor2linha<matriz[1][m]:
        maior_valor2linha=matriz[1][m]
print(f'O maior valor da segunda linha foi: {maior_valor2linha}')





