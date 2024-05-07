p1=float(input('Qual o preço do produto: '))
cores = {'vermelho': '\033[4;31m', 'limpo': '\033[m'}
m1=int(input(f'Qual a forma de pagamento: \n {'-'*12}\n(1)à vista dinheiro \n(2)à vista cartão \n(3)parcelado em 2x \n(4)parcelado em 3x \n'))
if m1 == 1:
    p1=p1-(p1/10)
elif m1 == 2:
    p1 = p1-(p1/20)
elif m1 == 3:
    p1 = p1
elif m1 == 4:
    p1=p1+(p1/5)
else:
    print(f'{cores["vermelho"]}ERROR{cores["limpo"]}')
if m1== 1 or m1== 2 or m1 == 3 or m1 == 4:
    print(f'O preço final ficará no valor de {p1:.2f}R$')