p=float(input('Qual o primeiro termo da PA: '))
r=float(input('Qual a razão da PA: '))
t=int(input('Quantos termos da sua PA você deseja: '))
termo=1

#Apresentar a PA com as variaveis cruas.
while termo<t+1:
    pa=p+r*termo
    print(f'{termo}º={pa}')
    termo+=1

#+termos da PA
t1=''
t2=0
#Checa se ele ainda quer termos:
while t1!='N':
    #Refaz a pergunta
    t1=str(input('Você deseja ver mais termos? [S/N] ')).upper()
    #Checa se a resposta e válida
    if t1!='S' and t1!='N':
        while t1!='S' and t1!='N':
            print('Insira uma resposta válida!')
            t1=str(input('Você deseja ver mais termos? [S/N] ')).upper()
    #Se a resposta for sim, perguntar quantos a mais e fazer o número de termos-t-1=o número de termos adicionados anteriormente.
    if t1=='S':
        t2=int(input('Quantos a mais: '))  
        t2+=termo-t-1
    #Se a resposta for sim, o laço acaba e escrevemos fim na tela
    elif t1=='N':
        print('Fim')
    #Mostrar os novo termos pedidos da PA
    if t1=='S':
        while termo<t+t2+1:
            pa=p+r*termo
            print(f'{termo}º={pa}')
            termo+=1