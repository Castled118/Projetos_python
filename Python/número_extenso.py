tupla = ('zero', 'um', 'dois','três', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
n=str(input('Digite um número: '))
while True:
    while not(n.isnumeric()):
        print('Insira um valor númerico!')
        n=str(input('Digite um número: '))
    n1=int(n)
    if not(20>=n1>=0):    
        while not(20>=n1>=0):
            print('Insira um valor inteiro válido!(0-20)')
            n=str(input('Digite um número: '))
            while not(n.isnumeric()):
                print('Insira um valor númerico!')
                n=str(input('Digite um número: '))
            n1=int(n)
    if n.isnumeric and 20>=n1>=0:
        break
print(tupla[n1])
