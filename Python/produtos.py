continuar=''
barato=''
produtos_1000=0
valor_barato=0
soma=0
while continuar!='N':
    nome_produto=str(input('Qual o nome do produto: ')).strip()
    i=str(input('Qual o preço do produto: R$ '))
    while not(i.isnumeric()):
        print('Insira um preço válido!')
        i=str(input('Qual o preço do produto: R$ ')).strip()
    preco_produto=int(i)
    if valor_barato == 0:
        barato=nome_produto
        valor_barato=preco_produto
    if preco_produto<valor_barato:
        valor_barato=preco_produto
        barato=nome_produto
    if preco_produto>1000:
        produtos_1000+=1
    soma+=preco_produto
    continuar=str(input('Você quer continuar? [S/N]')).upper().strip()
    while continuar not in 'SN':
        print('Insira um valor válido!')
        continuar=str(input('Você quer continuar? [S/N]')).upper().strip()
print('=-'*13)
print('FIM')
print('=-'*13)
print(f'O produto mais barato foi o {barato}.')
print(f'{produtos_1000} produto(s) custam mais que 1000 reais.')
print(f'A soma dos preços dos produtos foi de {soma}R$')
        