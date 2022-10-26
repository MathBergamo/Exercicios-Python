#PRIMEIRA TENTATIVA!

print('LEITOR NÚMERICO POR EXTENSO')

extenso = 'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze'\
    ,'quinze','dezesseis','dezessete','dezoito','dezenove','vinte'

usuario = int(input('Erro... Digite um número entre 0 e 20:'))
print(f'Você digitou o número: {extenso[usuario]}')

#RESOLUÇÃO FINAL
print('LEITOR DE NÚMERO POR EXTENSO')
n = -1
extenso = 'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze',\
          'quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'

while n < 0 or n > 20:
    n = int(input('Digite um número entre 0 e 20:'))
print(f'Você digitou o número: {extenso[n]}')

#SOLUÇÃO 2.0

print('LEITOR NÚMERICO POR EXTENSO')

tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    n = int(input('Digite um número:'))
    while n < 0 or n > 20:
        n = int(input('Erro.. Digite novamente:'))
    else:
        print(tupla[n])
    usuario = str(input('Desejar continuar?')).strip().lower()[0]
    if usuario in 'Ss':
        print('Voltando..\n')
    elif usuario in 'Nn':
        break
