#Pedir el nombre del jugador 1 y del jugador 2.
#Mostrar los puntos de vida iniciales de ambos jugadores.
#Indicar el turno que comienza
#Pedir al jugador 1 que elija una acción:
    #1 → Atacar.
    #2 → Defender.
#y pedir al jugador 2 que elija igual.
#Resolver el turno.
#Mostrar los puntos de vida de ambos jugadores después del ataque.
#Segundo turno igual, indicar que comienza, pedir jugador 1 y jugador 2. Resolver.
#Mostrar los puntos de vida de ambos jugadores después del ataque

jugador1=str(input("Jugador1:"))
jugador2=str(input("Jugador2:"))
print(jugador1 + " y " + jugador2, "ambos inician con 100HP")
Hp1=100
Hp2=100
atacar=25
defender=25
print("turno 1 comienza:" " " + jugador1)
elegir=str(input("atacar o defender:"))
if elegir==atacar:
    print(Hp2-atacar)
else:
    print(defender)


