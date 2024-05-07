p=str(input('Digite sua frase: ')).strip()
palavras = p.split()
junto= ''.join(palavras)
s = 1
inverso=''
for c in range (len(junto)-1,-1,-1):
    inverso+=junto[c]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo!')
