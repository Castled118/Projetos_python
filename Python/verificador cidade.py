s1=str(input('Qual cidade você nasceu: '))
s2=bool('santos' in ((s1.lstrip()).lower()) or 'santo' in ((s1.lstrip()).lower()))
if s2:
    print(f'\033[4;32;40m{s2}\033[m')
else:
    print(f'\033[4;31;40m{s2}\033[m')