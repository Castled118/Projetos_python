s=0
for c in range (0,3):
    n=(int(input('Digite um número: ')))
    if n%2!=0 and n%3==0 and 500>=n>=1:
        s+=n
print(s)