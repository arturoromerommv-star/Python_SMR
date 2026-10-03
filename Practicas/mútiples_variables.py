#Podemos asignar múltiples variables en una línea:
x, y, z="Blanco", "Banana", "Loco"
print(x)
print(y)
print(z)

#Puedes asignar el mismo valor a múltiples variables en una línea:
arco = espada = zeta = "Juan"
print(arco)
print(espada)
print(zeta) #Nos devuelve 3 veces Juan

#Si teiens una colección de variables en list, 
#tuple etc, Python le permite extraer los valores en variables, a esto se le llama desembalaje.
frutas = ["manzana", "Pera", "Sandía"]
a, b, c = frutas
print(a)
print(b)
print(c)