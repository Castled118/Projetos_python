n = int(input('Digite um número: '))
print('Fatorial usando o laço while: ')
c = 0
fatorial = 1
fatorial1 =1
while (n-c)!=1:
    c+=1
    fatorial*=(n-c)
fatorial*=n
print(f'O fatorial do número {n} é igual a {fatorial}')
print(f'{'-'*12}\n Fatorial usando o laço for: ')
for c in range (n,0,-1):
    fatorial1*=c
print(f'O fatorial do número {n} é igual a {fatorial1}')
    