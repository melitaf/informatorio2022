"""
DESAFÍO 4
Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado. 
Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6

"""

print("Haremos un cuadrado ecologico.")

c_verde = "|verde|"
c_blanco = "|blanco|"

pareja1 = c_blanco + c_verde
pareja2 = c_verde + c_blanco

altura = int(input("Ingresar la altura del cuadrado: \n"))
largo = int(input("Ingresar la largo del cuadrado: \n"))

print("El cuadrado ecologico queda: \n")
while altura > 0: #1 fila de cuadrado implica usar, 2 renglones de parejas.
	print(pareja1*largo)
	print(pareja2*largo)
	altura -= 1

