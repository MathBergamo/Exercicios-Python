def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except(ValueError,TypeError):
            print(f'\033[0;31mERRO!, informação inválida! \033[m')
        except(KeyboardInterrupt):
            print(f'\033[1;93mO Usuário preferiu não digitar um valor!\033[m')
            return 0
        else:
            return valor

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;93m{c}\033[m - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[1;32mSua opção:\033[m')
    return opc
