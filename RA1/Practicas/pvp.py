
#1.- Pedimos nombre
jugador1 = input("jugador1: ")
jugador2 = input("jugador2: ")
#2.-vida inicial
Hp1 = 100
Hp2 = 100
atacar = 25
defender = 25
print(jugador1 + " y " + jugador2 + " inician con 100hp")
#3.-Indicar el turno el turno que comienza
#4.-Pedir al jugador 1 que elija una acción:
    #1 → Atacar.
    #2 → Defender.
#5.-y pedir al jugador 2 que elija igual
print("Turno 1")
elegir1 = (input(jugador1 + " elija 2 para atacar y 1 para defender: "))
elegir2 = (input(jugador2 + " elija 2 para atacar y 1 para defender: "))
if elegir1 == "1":
    if elegir2 == "2":
     Hp2 = Hp2 - defender    
else:
    Hp2 = Hp2 - atacar
if elegir2 == "1":
    if elegir1 == "2":
         Hp1 = Hp1 - defender    
else:
    Hp1 = Hp1 - atacar
print("vida de " + jugador1 + ": " + str(Hp1))
print("vida de " + jugador2 + ": " + str(Hp2))
