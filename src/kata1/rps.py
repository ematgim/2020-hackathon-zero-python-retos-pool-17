from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
empatar = 'Empate!'
ganar = 'Ganaste!'
perder = 'Perdiste!'
def quienGana(player, ai):
    player = str(player).lower
    ai = str(ai).lower
    ganador = True
    if player == ai:
        return empatar
    else: 
        if player == options[1].lower and ai == options[2].lower: 
            ganador = False
        elif player == options[2].lower and ai == options[3].lower:
            ganador = False
        elif player == options[3].lower and ai == options[1].lower:
            ganador = False
        else:
            ganador = True
    
    if ganador:
        return ganar
    else:
        return perder


# Entry Point
def Game():
    
    winner = quienGana(player, ai)

    print(winner)

