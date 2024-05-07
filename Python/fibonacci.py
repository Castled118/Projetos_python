n1=int(input('Qual o primeiro termo da sua sequencia fibonacci: '))
n2=int(input('Quantos termos você quer: '))
termos=0
t1=0
t2=n1
t3=t2+t1
while termos<=n2-1:
    termos+=1
    if termos<=2:
        print(f'{termos}->{n1}')
    if termos>2: #n1 = 2
        print(f'{termos}->{t3}')
    t3=t1+t2
    t1=t2
    t2=t3
        
     