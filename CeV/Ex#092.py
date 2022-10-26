#1 SOLUÇÃO
from datetime import datetime

pessoa = {'nome': str(input('Nome:').capitalize().strip()),
          'nascimento': int(input('Ano de nascimento:')),
          'ctps': int(input('Carteira de trabalho (0 Caso não houver):'))}
idade = datetime.today().year - pessoa['nascimento']

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação:'))
    pessoa['salario'] = int(input('Salário: R$'))
    print(30*'-=')
    print(f'*- Nome: {pessoa["nome"]}')
    print(f'*- idade: {datetime.now().year - pessoa["nascimento"]}')
    print(f'*- Carteira de trabalho: {pessoa["ctps"]}')
    print(f'*- Ano da contratação: {pessoa["contratacao"]}')
    print(f'*- Salário: R${pessoa["salario"]}')
    print(f'*- Idade de aposentadoria: {idade + (pessoa["contratacao"]+35) - datetime.now().year}')
else:
    print(30*'-=')
    print(f'-* Nome: {pessoa["nome"]}')
    print(f'-* Idade: {datetime.now().year - pessoa["nascimento"]}')
    print(f'-* Carteira de trabalho: {pessoa["ctps"]}')

