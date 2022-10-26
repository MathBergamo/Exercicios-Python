def notas(*msg,sit=False):
    """
    Função para analisar as notas de uma sala.
    :param msg: Parâmetro formal que recebe as notas dos alunos.
    :param sit: Irá mostrar a situação atual da sala de acordo com a média. (opcional)
    :return: Retorna um dicionário com as informações da sala.
    """
    alunos = {}
    alunos['total'] = len(msg)
    alunos['maior'] = max(msg)
    alunos['menor'] = min(msg)
    alunos['media'] = sum(msg) / len(msg)
    if sit:
        if alunos['media'] >= 7:
            alunos['situaçao'] = 'BOA'
        elif alunos['media'] >= 5:
            alunos['situaçao'] = 'RAZOÁVEL'
        else:
            alunos['situaçao'] = 'RUIM'
    return f'{alunos}'

turma = notas(5.5,2.5,1.5,sit=True)
print(f'Turma = {turma}')
print(help(notas))

