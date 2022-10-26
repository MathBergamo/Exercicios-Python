m = float(input('Digite uma distância em Metros: '))
ml = m*1000 #milimetros
cm = m*100 #centimetros
dc = m*10 #decimetros
dm = m/10 #decâmetros
hc = m/100 #hectômetros
km = m/1000 #kilometros

print(f'A medida de {m} metros é igual a:\n{km} Kilometros \n{hc} Hectômetros\n{dm} Decâmetros\n{dc} Decimetros')
print(f'{cm} Centimetros\n{ml} Milimetros')
