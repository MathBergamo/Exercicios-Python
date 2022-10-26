# 1 SOLUÇÃO
exp = str(input('Digite sua expressão:'))
entrada = []

for simb in exp:
    if simb == '(':
        entrada.append('(')
    elif simb == ')':
        if len(entrada) > 0:
            entrada.pop()
        else:
            entrada.append(')')
            break

if len(entrada) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')

