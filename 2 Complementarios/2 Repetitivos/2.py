#2) Desarrollar una solución que calcule la suma de los cuadrados de los n primeros números naturales: 1 + 22 + 32 +… + n2.
# Existe en matematicas una formula para resolver esto. Pero no ocupariamos los bucles, que es la finalidad del ejercicio.

# Sin formula para resolverlo, usando un bucle for:
print("Solucion: ")

cuadrados_n_numeros = []

n_primeros = int(input("Ingrese un cuantos numeros naturales al cuadrado quiere sumar: "))


for numeros_cuadrados in range(n_primeros):
	cuadrados_n = n_primeros**2
	cuadrados_n_numeros.append(int(cuadrados_n))
	print(cuadrados_n_numeros)
	n_primeros -= 1
print(sum(cuadrados_n_numeros))

