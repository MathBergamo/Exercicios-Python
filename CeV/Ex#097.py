#PRIMEIRA TENTATIVA
def escreva(txt):
    print(len(txt)*'~')
    print(f'{txt:^}')
    print(len(txt)*'~')


escreva('Colaboradora')
escreva('Carambolas')
escreva('Churimol')
escreva('Cachi')
escreva('Chu')

#OUTRA SOLUÇÃO

def escreva(txt):
    t = len(txt) + 4
    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)

escreva('Cachimbol')
escreva('Caco')
escreva('Carlos Drummond Daniel de Andrade')

def escreva(txt):
    t = len(txt) + 4
    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)
