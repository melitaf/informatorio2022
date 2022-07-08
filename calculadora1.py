print("Mucho gusto. Vamos a realizar operaciones matematicas.")

print("Suma")
print("Resta")
print("Multiplicacion")
print("Division")

operaciones_a_realizar = input("Ingrese la operacion que quiere realizar: ")

agregar_numero = input("Quiere agregar un numero: ")

if operaciones_a_realizar.lower() == "suma":
	suma = 0
	while agregar_numero.lower() == "si":
		
		numero = float(input("Ingrese los numeros a sumar: "))
		suma += numero
		agregar_numero = input("Quiere agregar un numero: ")


		if agregar_numero.lower() == "no":
			print("La suma total es de: ", suma)	
			break

elif operaciones_a_realizar.lower() == "resta":
	resta = 0
	while agregar_numero.lower() == "si":
		
		numero = float(input("Ingrese los numeros a restar: "))
		resta = resta - numero
		agregar_numero = input("Quiere agregar un numero: ")


		if agregar_numero.lower() == "no":
			print("La resta total es de: ", resta)	
			break

else:
	print("No se realiza otra oper")

