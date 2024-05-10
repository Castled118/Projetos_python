import math
x=0
y=0
resultados=[]
resultados_parcial=[]

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for i in range(0,1972246):
    x+=1
    if primo(x) and x!=5:
        if 1008%(x+5)==0:
            y=((8*(x**2))-40*x+199-(1008/(x+5)))
            resultados_parcial.append(x)
            resultados_parcial.append(int(y))
            resultados.append(resultados_parcial[:])
            print(resultados_parcial)
            resultados_parcial.clear()
print(resultados)
