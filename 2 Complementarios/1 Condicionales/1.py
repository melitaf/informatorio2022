#Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.

print("\t=================")
print("\tVamos a ordenar:")
print("\t=================\n")

num_1 = float(input("Ingrese un numero: "))
num_2 = float(input("Ingrese un numero: "))
num_3 = float(input("Ingrese un numero: "))

if num_1 >= num_2 and num_1 >= num_3 and num_2 >= num_3:
	print(num_1)
	print(num_2)
	print(num_3)
elif num_1 >= num_2 and num_1 >= num_3 and num_3 >= num_2:
	print(num_1)
	print(num_3)
	print(num_2)
elif num_2 >= num_1 and num_2 >= num_3 and num_1 >= num_3:
	print(num_2)
	print(num_1)
	print(num_3)
elif num_2 >= num_1 and num_2 >= num_3 and num_3 >= num_1:
	print(num_2)
	print(num_3)
	print(num_1)
elif num_3 >= num_1 and num_3 >= num_2 and num_1 >= num_2:
	print(num_3)
	print(num_1)
	print(num_2)
else:
	print(num_3)
	print(num_2)
	print(num_1)