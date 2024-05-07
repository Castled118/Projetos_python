lista=[]
lista_pares=[]
lista_impares=[]
for y in range(1,8):
    numero=str(input(f'Digite o {y}º valor: '))
    while not(numero.isnumeric()):
        numero=str(input('Digite um valor válido'))
    numero=int(numero)
    if numero%2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
lista_pares.sort()
lista_impares.sort()
lista.append(lista_impares)
lista.append(lista_pares)
print('-'*50)
print('Os números pares foram, ',end='')
for n in lista[1]:
    print(n,end=' ')
print('\nOs números impares foram, ',end='')
for k in lista[0]:
    print(k,end=' ')