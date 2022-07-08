# 6) Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números, tal que el segundo sea mayor o igual que el primero.

print("#############################")
print("Ingrese una serie de numeros.")
print("#############################\n")

serie_numero = []
mayor = 0

numero = int(input("Ingrese un numero, o ingrese 0 para salir: "))

while numero != 0:
	if numero % 2 == 0 and (numero >= mayor):
		mayor = numero
		serie_numero.append(numero)
		print(serie_numero)
	numero = int(input("Ingrese un numero, o ingrese 0 para salir: \n"))

print(f"La lista tiene {len(serie_numero)} multiplos de 2.\n")
print(f"La lista tiene una suma total de: {sum(serie_numero)}.\n")