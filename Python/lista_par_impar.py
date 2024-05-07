lista=[]
resposta=''
while resposta!='N':
    n=str(input('Digite um número: '))
    while not(n.isnumeric):
        print('Digite um valor válido: ')
    n=int(n)
    lista.append(n)
    resposta=str(input('Você deseja continuar? [S/N] ')).upper().strip()
    while resposta not in 'SN':
        resposta=str(input('Insira uma resposta válida, você deseja continuar? [S/N] '))
lista_impar=[]
lista_par=[]
for numero in lista:
    if numero%2==0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
print(f'A lista original foi {lista}')
print(f'A lista de pares foi {lista_par}')
print(f'A lista de impares foi {lista_impar}')