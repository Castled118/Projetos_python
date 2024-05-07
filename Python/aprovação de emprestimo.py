from math import ceil
casa =int(input('Qual o valor da casa: '))
salario = float(input('Qual o valor do seu salário: '))
tempo  = int(input('Em quantos anos você pretende pagar a casa: '))
mensalidade = casa/ (tempo*12)
if mensalidade>(salario*3/10):
    print(f'Seu empréstimo foi \033[4;31mnegado!\033[m Você pode ou passar a ganhar {mensalidade*(10/3):.2f} ou você pode optar por pagar no tempo de {((ceil(casa/(3/10*salario)))/12):.2f} anos ({ceil(casa/(3/10*salario))} meses)')
else: 
    print(f'Seu empréstimo foi \033[4;32maceito!\033[m Você precisará pagar {tempo*12} prestações de {mensalidade:.2f}R$')