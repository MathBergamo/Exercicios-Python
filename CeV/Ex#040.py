n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua seguna nota: '))
media = (n1+n2) / 2

if media >= 7.0:
    print(f'Você teve a média de {media} e está APROVADO! \n {5*"=-"}PARABÉNS{5*"-="}')
elif 6.99 > media >= 5.0:
    print(f'Você está de RECUPERAÇÃO!\n Média: {media}')
else:
    print(f'Você está REPROVADO!\n Média: {media}')

#Irá verificar se um aluno está aprovado, de recuperação ou reprovado de acordo com a média.