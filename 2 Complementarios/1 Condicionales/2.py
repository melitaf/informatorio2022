#Desarrolle un programa que permita determinar si un número X ingresado es par o impar.

print("\t=======================")
print("\tDeterminamos si es par o impar")
print("\t=======================\n")

numero = int(input("Ingrese el numero a comprobar: \n"))

if numero % 2 == 0:
	print(f"\nEl numero ingresado: {numero} es par.")
else:
	print(f"\nEl numero ingresado: {numero} es impar.")