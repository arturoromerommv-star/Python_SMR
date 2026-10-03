
#1.- Pedimos nombre
jugador1 = input("jugador1: ")
jugador2 = input("jugador2: ")
#2.-vida inicial
Hp1 = 100
Hp2 = 100
atacar = 25
defender = 10
print(jugador1 + " y " + jugador2 + " inician con 100hp")
#3.-Indicar el turno el turno que comienza
#4.-Pedir al jugador 1 que elija una acción:
    #1 → Atacar.
    #2 → Defender.
#5.-y pedir al jugador 2 que elija igual
print("Turno 1")
elegir1 = int(input(jugador1 + " elija 1 para atacar y 2 para defender: "))
elegir2 = int(input(jugador2 + " elija 1 para atacar y 2 para defender: "))
