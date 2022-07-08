"""
7) Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B.
El programa no permitirá introducir valores negativos para A y B y verificará que A es menor que B.
Si A es mayor que B, se deben intercambiar los valores.
"""

print("#######################")
print("Ingrese 2 valores.")
print("#######################\n")

#Condiciones
valor_A = int(input("Ingrese un valor desde el cual inicia a buscarse multiplos: \n"))
while valor_A<0:
	print("Ingrese un valor positivo(+)")
	valor_A = int(input("Ingrese un valor desde el cual inicia a buscarse multiplos: \n"))

valor_B = int(input("Ingrese un valor desde el cual finaliza la busqueda de multiplos: \n"))
while valor_B<0:
	print("Ingrese un valor positivo(+)")
	valor_B = int(input("Ingrese un valor desde el cual finaliza la busqueda de multiplos: \n"))


#Lista a incrementar con multiplos dentro del rango ingresado:
multiplos_de_5 = []

for numero in range(valor_A, valor_B):
	if numero % 5 == 0:
		multiplos_de_5.append(numero)
print(multiplos_de_5)

print(f"\nLa suma de los multiplos de 5, dentro del rango ingresado es de {sum(multiplos_de_5)}.\n")


"""
Para verificar que A es menor que B:

if valor_A > valor_B:
	rango_ab = (valor_A, valor_B)
else:
	rango_ab = (valor_B, valor_A)

for numero in range(int(rango_ab)):
	if numero % 5 == 0:
		multiplos_de_5.append(numero)
print(multiplos_de_5)

"""