from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano
    if 18 <= idade <= 65:
        return f'Aos {idade} anos, o VOTO É OBRIGATÓRIO!'
    elif 16 <= idade <= 17 or idade > 65:
        return f'Aos {idade} anos, o VOTO É OPCIONAL!'
    elif idade <= 15:
        return f'Aos {idade} anos, NÃO VOTA!'


usuario = int(input('Em que ano você nasceu?'))
print(30*'-')
print(voto(usuario))
