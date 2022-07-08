"""
---------------------------------  DESAFÍO 4
Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.

Ingredientes comunes: Verduras y berenjena.
Ingredientes Receta 1: Lentejas y apio.
Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú 
con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta. 
Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.

"""

print("Vamos a cocinarle:")
a = "a) receta1"
b = "b) receta2"
receta1 = "Ingredientes Receta 1: Lentejas y apio."
receta2 = "Ingredientes Receta 2: Morrón y Cebolla.."
ingredientes_comunes = "Ingredientes comunes: Verduras y berenjena."
ingrediente_comun1 = "1) Verduras"
ingrediente_comun2 = "2) berenjena"

print(a)
print(b)

receta_elegida = input("Elija la receta a realizar: ")

if receta_elegida.lower() == "a":
    print("Elija que ingredientes comunes va a utilizar: ")
    print(ingrediente_comun1)
    print(ingrediente_comun2)
    terceringrediente=int(input("Ingrese el 3er ingrediente que le añadira (1 o 2): "))
    if terceringrediente == 1:
        print("Los ingredientes a utilizar son Lentejas, Apio y Verduras")
    else:
        print("Los ingredientes a utilizar son Lentejas, Apio y berenjena.")

if receta_elegida.lower() == "b":
    print("Elija que ingredientes comunes va a utilizar: ")
    print(ingrediente_comun1)
    print(ingrediente_comun2)
    terceringrediente=int(input("Ingrese el 3er ingrediente que le añadira (1 o 2): "))
    if terceringrediente == 1:
        print("Los ingredientes a utilizar son Morron, Cebolla y Verduras")
    else:
        print("Los ingredientes a utilizar son Morron, Cebolla y berenjena.")
        
