km = float(input('Digite a distância viajada em km:'))
print(f'Você irá realizar uma viagem de {km}Km')

if km <= 200:
    preco = km * 0.50
    print(f'Você irá pagar R${preco:.2f} ')
else:
    preco = km * 0.45
    print(f'Após passar mais de 200km, você irá pagar o preço promocional de R${preco:.2f}')
