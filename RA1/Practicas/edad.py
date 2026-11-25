#Crea el diagrama de flujo para: 

#Pida al usuario su nombre.
#Pida su edad.
#Muestre un saludo con su nombre.
#Si tiene 18 años o más, muestre: Eres mayor de edad.
#Si tiene menos de 18, simplemente muestre su edad.

nombre=(input("¿Como te llamas?"))
print("Muy buenas caballero/a" + nombre) #Añadir + para agregar una variable.
edad=int(input("Que edad tienes¿?"))
if edad >=18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")
