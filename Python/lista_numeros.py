from random import randint
k=(randint(1,1000),randint(1,1000),randint(1,1000),randint(1,1000),randint(1,1000))
print('Os números sortados foram: ',end='')
for n in k:
    print(f'{n}',end=' ')
j=(sorted(k))
print(f'sendo o menor {j[0]} e o maior {j[len(k)-1]}!')
