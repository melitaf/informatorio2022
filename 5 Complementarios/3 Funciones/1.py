"""
Ejercicio 1: Triángulos

Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo como sus parámetros y 
devuelva la hipotenusa del triángulo, calculada usando el teorema de Pitágoras, como resultado de la función. 
Incluya un programa principal que lea las longitudes de los lados más cortos de un triángulo rectángulo del usuario, 
use su función para calcular la longitud de la hipotenusa y muestre el resultado.
"""

print("\t===========================")
print("\tVamos a calcular la hipotenusa.")
print("\t===========================\n")

lado1 = float(input("Ingrese el valor del primer lado: "))
lado2 = float(input("Ingrese el valor del segundo lado: "))

def triangulo(a, b):
	hipotenusa = ((a**2)+(b**2))**(1/2)
	return print(f"\nEl valor de la hipotenusa es de {hipotenusa}.")


triangulo(lado1, lado2)