frase = str(input('Digite uma frase:')).lower().strip()

print(f'A letra (A) aparece: {frase.count("a")}x')
print(f'A primeira letra (A) aparece na posição: {frase.find("a")+1}º')
print(f'A última letra (A) aparece na posição: {(frase.rfind("a")+1)}º')

#find irá mostrar aonde foi encontrado o primeiro valor "a"
#rfind irá mostrar aonde foi o encontrado o último valor "a"