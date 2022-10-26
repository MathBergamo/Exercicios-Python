vel = float(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'Você foi multado no valor de: R${multa}, o limite da via é 80km/h ')
    print('Preste atenção na próxima vez!')
print('Tenha um bom dia.')

#Caso a velocidade do carro ultrapasse os 80km, o motorista irá receber uma multa de 7 reais para cada km ultrapassado