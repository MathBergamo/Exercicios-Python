from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Lista de cadastrados','Cadastrar','Sair do sistema'])
    if resposta == 1:
        #opção de listar pessoas cadastradas
        lerarquivo(arq)
    elif resposta == 2:
        #opção de cadastrar pessoas
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaint('Idade:')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        #opção de sair do sistema
        cabeçalho('Saindo do sistema... Até mais!')
        break
    else:
        print(f'\033[1;31mERRO! Digite uma opção válida! \033[m')
    sleep(2)
