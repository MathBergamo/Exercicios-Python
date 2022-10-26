def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except(ValueError,TypeError):
            print(f'\033[0;31mERRO!, informação inválida! \033[m')
        except(KeyboardInterrupt):
            print(f'\033[1;93mO Usuário preferiu não digitar um valor!\033[m')
            return (f'O número \"INTEIRO\" digitado foi: \033[1;93m Sem valores registrados\033[m')
        else:
            return f'O número \"INTEIRO\" digitado foi: {valor}'


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except(ValueError,TypeError):
            print(f'\033[0;31mERRO!, informação inválida! \033[m')
        except(KeyboardInterrupt):
            print(f'\033[1;93mO Usuário preferiu não digitar um valor!\033[m')
            return (f'O número \"REAL\" digitado foi: \033[1;93mSem valores registrados\033[m')
        else:
            return f'O número \"REAL\" digitado foi: {valor}'


n = leiaint('Digite um número inteiro:')
n1 = leiafloat('Digite um número real:')
print(f'{n}\n{n1}')
