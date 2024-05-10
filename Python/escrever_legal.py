from time import sleep
palavra=str(input('Qual palavra você deseja escrever de forma legal: '))
alfabeto=' abcdefghijklmnoprstuvwxyzãáàíõóé '
resultado=''
for i in palavra:
    for k in alfabeto:
        sleep(0.02)
        if k==i or k.upper()==i:
            if k.upper()==i:
                resultado+=k.upper()
            else:
                resultado+=k
            print(resultado)
        else:
            print(resultado+k)