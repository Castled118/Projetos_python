tupla=('folguedo','mirim','burocracia','recapitulação','recompensa','aeiou')
vogais=('A','E','I','O','U')
for a in tupla:
    print(f'\nNa palavara {a} temos: ',end='')
    a1=a.upper()
    for b in vogais:
       if a1.count(b)>0:
           print(a[a1.index(b)],end=' ')
print(f'\n{'-'*50}')
for c in tupla:
    print(f'\nNa palavra {c} temos: ', end='')
    c1 = c.upper()
    for char in c:
        if char.upper() in vogais:
            print(char, end=' ')