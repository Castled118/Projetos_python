n1=int(input('Qual número você deseja: '))
s1=0
for c in range (1,n1+1):
    if c!=1 and c!=n1:    
        if n1%c==0:       
            s1+=1        
if s1==0:
    print('O número é primo!')
else:
    print('Ele não é primo!')
