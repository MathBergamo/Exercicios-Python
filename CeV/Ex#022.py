nome = str(input('Digite seu nome completo: ')).strip().title()

print(f"{10*'-='}\n{2*' '+nome}\n{10*'-='}\nSeu nome completo tem: {len(nome)-nome.count(' ')} "
      f"letras \nE seu primeiro nome tem: {len(nome.split()[0])} letras")

#len(nome)-nome.count(' ') - Irá ver quantas letras tem o nome, contar e retirar os espaços vazios.
#split torna as strings em formato de lista, refazendo a contagem dos parâmetros. Permite contar o primeiro nome individualmente