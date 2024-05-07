print('-'*34)
print('       Listagem de produtos!')
print('-'*34)
produtos=('Pão', 2,'Queijo', 3, 'Feijão', 7, 'Compasso', 15,'Celular', 1500,'Carteira',40)
for n in range(0,len(produtos),2):
    print(produtos[n],end='.'*(30-(len(produtos[n]))-(len(str(produtos[n+1]))-2)))
    #print(f'{produtos[n]:.<30}',end='')
    print(f'{produtos[n+1]}R$')
print('-'*34)
