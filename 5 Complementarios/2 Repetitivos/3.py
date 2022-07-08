#3) Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas.

print("##########################")
print("Bienvenido, hagamos calculos.")
print("##########################\n")
print("Vamos a realizar una multiplicacion: \n")

""" 
El multiplicador es el que se escribe primero, ya que cuando se escribe 4 x 5 y 
se interpreta el signo de multiplicar como sustituto de “veces”, 4 x 5 significa 4 veces 5 o 5 +5 +5 +5, 
por lo que el 4 es el multiplicador y el 5 el multiplicando.
"""
#variables:
multiplicacion = []
multiplicador = int(input("Ingrese el valor del multiplicador: ")) #Para saber el rango que tendra mi lista.
multiplicando = float(input("Ingrese el valor del multiplicando: ")) #Se va a ir agregando de a uno por vez.

#Solucion con for:
for numero in range(multiplicador):
	multiplicacion.append(multiplicando)
print(f"\nEl resultado de la multiplicacion es: {sum(multiplicacion)}")
