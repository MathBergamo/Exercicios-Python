seg1 = float(input('Diga o valor do primeiro segmento: '))
seg2 = float(input('Diga o valor do segundo segmento: '))
seg3 = float(input('Diga o valor do terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1+seg3 and seg3 < seg1+seg2:
    print('É possível formar um triângulo com essas medidas \n')
    if seg1 == seg2 == seg3:
        print('É um triângulo EQUILÁTERO')
    elif seg1 != seg2 != seg3 != seg1:
        print('É um triângulo ESCALENO')
    elif seg1 == seg2 != seg3 or seg2 == seg3 != seg1 or seg1 == seg3 != seg2:
        print('É um triângulo ISÓCELES')
else:
    print('Não é possível formar um triângulo')

#Irá informar o tipo de triângulo registrado de acordo com os segmentos