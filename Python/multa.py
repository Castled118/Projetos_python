n1=int(input('Quantos metros ele percorreu: '))
n2=int(input('Em quantos segundos: '))
n3= (n1/n2)*3.6
if n3 <= 80:
    print(f'O carro estava dentro da velocidade permitida: {n3:.2f} km/h')
else:
    print(f'O carro ultrapassou a velocidade permitida, estando a {n3} km/h e terá de pagar uma multa de {((n3-80)*7):.2f}R$')