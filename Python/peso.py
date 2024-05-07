maior=0
menor=0
for c in range (0,5):
    n1= float(input('Qual o seu peso em kg: '))
    if c == 0:
        maior = menor = n1
    elif c != 0 and n1>maior:
        maior = n1
    elif c != 0 and n1<menor:
        menor = n1
print(f'O maior peso foi de {maior}Kg e o menor foi de {menor}Kg')