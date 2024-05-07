lista = []
for _ in range(5):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    for i in range(len(lista) - 1, 0, -1):
        if lista[i] < lista[i - 1]:
            a=lista[i-1]
            b=lista[i]
            lista[i]=a
            lista[i-1]=b
        else:
            break
print(lista)

