def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO \"{entrada}\"\033[m é inválido!')
        else:
            valido = True
            return float(entrada)
