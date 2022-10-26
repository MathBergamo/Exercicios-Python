print('\nA seguir, iremos apresentar valores utilizados pelo calculo IMC (Índice de Massa Corporal)\n')

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / altura**2

if imc < 18.5:
    print(f'O IMC de {imc:.1f} é considerado abaixo do peso ideal. Os valores para o peso ideal é à partir de 18.5')
elif imc < 25:
    print(f'O IMC de {imc:.1f} é considerado peso ideal. Os valores para o peso ideal estão entre 18.5 e 25.0 ')
elif imc < 30:
    print(f'O IMC de {imc:.1f} é considerado sobrepeso. Os valores para o sobrepeso são entre 25.0 até 30.0')
elif imc < 40:
    print(f'O IMC de {imc:.1f} é considerado obesidade. Os valores para obesidade estão entre 30.0 até 40.0 ')
else:
    print(f'O IMC de {imc:.1f} é considerado obesidade mórbida. Os valores para obesidade morbida são', end=' ')
    print('considerados à partir de 40.0 e superiores.')

#Cálculo de IMC