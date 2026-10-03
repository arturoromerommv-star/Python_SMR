#Crea el programa en google colab según el diagrama de flujo:
#El nombre del jugador.
#Su puntuación.
#El programa debe mostrar un mensaje personalizado y clasificar la puntuación:
#Si la puntuación es 1000 o superior, mostrar ¡Puntuación excelente!
#Si está entre 500 y 999, mostrar ¡Muy bien!
#Si es inferior a 500, mostrar Puedes mejorar.

nombre=str(input("Nombre:"))
print("Buenas" + nombre)
puntos=int(input("puntuación:"))
if puntos >=1000:
    print("¡Puntuación excelente!")
if puntos >=500 and puntos <=999:
    print("¡Muy bien!")
if puntos <500:
    print("Puedes mejorar")