times= ('Bragantino','Flamengo','Botafogo','Athletico','Grêmio','Inter',
        'Atlético-MG','Fortaleza','Bahia','Fluminense','Palmeiras','Cruzeiro','Juventude','São Paulo',
        'Vasco da Gama','Criciúma','Vitória','Corinthias','Atlético-GO','Cuiabá')
print(f'O vasco da gama está na posição {times.index('Vasco da Gama')+1}')
print(f'Os 5 últimos times são {times[15:]}')
print(f'Os 5 primeiros times são {times[:5]}')
print(f'Os times em ordem alfabética são {sorted(times)}')