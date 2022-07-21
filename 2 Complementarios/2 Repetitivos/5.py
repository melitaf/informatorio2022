# 5) Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar. 
# El ciclo debe finalizar cuando el usuario ingresa 0.

print("Determinacion de numeros.\n")

numero = int(input("Ingrese un numero, o ingrese 0 para salir: "))
while numero != 0:
	if numero % 2 == 0:
		print("El número es par")
	else:
		print("El numero es impar.")
	numero = int(input("Ingrese un numero, o ingrese 0 para salir: "))
