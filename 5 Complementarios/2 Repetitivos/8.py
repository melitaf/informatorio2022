"""
8) Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. 
El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee.
"""

print("#############################")
print("Vamos a calcular el total de la compra.")
print("#############################\n")

#Variables:
agregar_producto = str(input("Quiere ingresar un producto? ('si' para añadir//cualquier letra para salir.): \n"))
lista_valor = []

#Condiciones:

while agregar_producto.lower()== "si":
	cantidad_pto = int(input("Ingrese la cantidad requerida del producto: \n"))
	precio_pto = float(input("Ingrese el precio del producto: \n"))
	total_pto = cantidad_pto*precio_pto
	lista_valor.append(total_pto)
	print(lista_valor)
	agregar_producto = str(input("Quiere ingresar un producto? ('si' para añadir//cualquier letra para salir.): \n"))



print(f"\nEl total de la compra es ${sum(lista_valor)}.")