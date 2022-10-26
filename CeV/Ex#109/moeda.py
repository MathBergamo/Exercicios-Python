def metade(num = 0,formato=False):
    """
    Coloca valor pela metade.
    :param num: Recebe um valor
    :param formato: Formata o valor para monetário
    :return: Retorna o valor sem formatação ou com formatação de acordo com a condição falsa ou verdadeira
    """
    num /= 2
    return metade if not formato else moeda(num)


def dobro(num = 0,formato=False):
    """
    Dobra o valor
    :param num: Recebe um valor
    :param formato: Formata o valor para monetário
    :return: Retorna o valor sem formatação ou com formatação de acordo com a condição falsa ou verdadeira
    """
    num *= 2
    return num if not formato else moeda(num)


def aumentar(num= 0,taxa=0,formato=False):
    """
    Aumenta o valor.
    :param num: Recebe um valor
    :param taxa: Adiciona um valor percentual ao valor total.
    :param formato: Formata o valor para monetário
    :return:Retorna o valor sem formatação ou com formatação de acordo com a condição falsa ou verdadeira
    """
    num += (num*taxa) / 100
    return num if not formato else moeda(num)


def diminuir(num = 0,taxa=0,formato=False):
    """
    Diminui o valor
    :param num:
    :param taxa:
    :param formato: Formata o valor para monetário
    :return: Retorna o valor sem formatação ou com formatação de acordo com a condição falsa ou verdadeira
    """
    num -= (num*taxa) / 100
    return num if not formato else moeda(num)


def moeda(num = 0, moeda = 'R$'):
    """
    Formata o valor.
    :param num: Recebe um valor
    :param moeda: Formatação para valor monetário REAL
    :return: retorna o valor formatado
    """
    return f'{moeda}{num:.2f}'.replace('.',',')
