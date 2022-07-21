"""
Desafío 2

Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:
Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
Si ambos números son iguales, debe devolver el nombre de ambas.
"""

ciudad1 = str(input("Ingrese el nombre de la primer ciudad ciudad a comparar: "))
ciudad2 = str(input("Ingrese el nombre de la segunda ciudad ciudad a comparar: "))

a = float(input(f"Ingrese la cantidad recilada por {ciudad1}: "))
b = float(input(f"Ingrese la cantidad recilada por {ciudad2}: "))

def relacion(a, b):

	if a>b:
		return print(f"\nLa ciudad que reciclo mas es: {ciudad1.lower()}.")
	else:
		return print(f"\nLa ciudad que reciclo mas es: {ciudad2.lower()}.")

relacion(a, b)