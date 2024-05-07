while True:
    n=int(input('Qual número você deseja: '))
    if n<0:
        break
    for c in range(1,11):
        print(f'{c}º --> {n*c}')
print('\033[4;31mFIM\033[m')