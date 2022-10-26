def fatorial(num,mostrar=False):
    '''
    Calcula o fatorial de um número
    :param num: Parâmetro que recebe o número para ser calculado a fatorial
    :param mostrar: Parâmetro para escolher se irá ser apresentado o calculo ou não.
    :return: Retorno do valor da fatorial
    '''
    f = 1
    for c in range(num, 0, -1):
        if mostrar:
            print(f'{c}',end=' x ' if c > 1 else ' = ')
        f *= c
    return f

usuario = int(input('Digite um número:'))
calculo = bool(input('Deseja ver o calculo? [Não digite nada se não quiser ver]'))
print(fatorial(usuario,calculo))
help(fatorial)
