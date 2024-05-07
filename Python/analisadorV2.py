print('-='*13)
print('CADASTRE UMA PESSOA')
print('-='*13)
cont=''
s=''
pes_18=0
homem=0
F_20=0
while cont!='N':
    s=str(input('Sexo: [M/F] ')).upper().strip()
    while s!='M' and  s!='F':
        print('Insira um sexo válido!')
        s=str(input('Sexo: [M/F] ')).upper().strip()
    i=str(input('Idade: '))
    while not(i.isnumeric()):
        print('Insira uma idade válida!')
        i=str(input('Idade: '))
    i2=int(i)
    cont=str(input('Você quer continuar? [S/N]')).upper().strip()
    while cont != 'S' and cont!= 'N':
        print('Insira uma resposta válida!')
        cont=str(input('Você quer continuar? [S/N]')).upper().strip()
    if i2>=18:
        pes_18+=1
    if s=='M':
        homem+=1
    if s=='F' and i2 >=20:
        F_20+=1
print('='*13,'\nFIM DO PROGRAMA\n')
print('='*13)
print(f'Você cadastrou {pes_18} pessoas com +18 anos, {homem} homens e {F_20} mulheres com +20 anos!')


        
    

        


    


