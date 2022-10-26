def metade(num = 0):
    metade = num/2
    return metade

def dobro(num = 0):
    dobrar = num*2
    return dobrar

def aumentar(num= 0):
    aumento = num *0.10
    return num+aumento

def diminuir(num = 0):
    diminuicao = num*0.13
    return num - diminuicao

def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')
