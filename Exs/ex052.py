def detector_primo(num):
    contagem = 0
    for c in range(1, num+1):
        if num % c == 0:
            contagem += 1
    if contagem > 2:
        return False
    else:
        return True


num = detector_primo(int(input('Digite um número:')))

if num == False:
    print('O número não é primo')
else:
    print('O número é primo')

