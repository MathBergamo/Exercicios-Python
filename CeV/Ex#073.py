times = 'Corintinhans','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco da Gama','Chapecoense','Atlético-MG',\
        'Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC-Vitória','Coritiba','Avaí',\
        'Ponte Preta','Atlético-GO'

print(f'Lista dos primeiros 20 colocados do Brasileirão de 2017{times}\n')
print(f'Primeiros 5º colocados:{times[:5]}')
print(f'Últimos 4º colocados:{times[-4:]}')
print(f'Lista em ordem alfabética:{sorted(times)}')
print(f'O Chapecoense está em {times.index("Chapecoense")+1}º lugar!')
