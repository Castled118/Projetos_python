
p1=float(input('Qual o seu peso: '))
a1=float(input('Qual a sua altura em metros: '))
IMC = p1/a1**2
if IMC < 18.5:
    print('Você está abaixo do peso ideal!')
elif 25 > IMC >=18.5:
    print('Você está no peso ideal!')
elif 30 > IMC >= 25:
    print('Você está acima do peso')
elif 40>IMC>=30:
    print('Você tem obesidade!')
elif IMC >= 40:
    print('Você possui obesidade mórbida!')