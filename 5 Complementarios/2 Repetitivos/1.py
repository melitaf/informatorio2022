#1) Determinar el número mayor de 10 números ingresados.

"""
#Con while

print("Vamos a solicitarle agregar 10 numeros: ")
while True:

	n1= float(input("Ingrese un numero: "))
	n2= float(input("Ingrese un numero: "))
	n3= float(input("Ingrese un numero: "))
	n4= float(input("Ingrese un numero: "))
	n5= float(input("Ingrese un numero: "))
	n6= float(input("Ingrese un numero: "))
	n7= float(input("Ingrese un numero: "))
	n8= float(input("Ingrese un numero: "))
	n9= float(input("Ingrese un numero: "))
	n10= float(input("Ingrese un numero: "))

	
	if n1>n2 and n1>n3 and n1>n4 and n1>n5 and n1>n6 and n1>n7 and n1>n8 and n1>n9 and n1>n10:
		maximo = n1
	elif n2>n1 and n2>n3 and n2>n4 and n2>n5 and n2>n6 and n2>n7 and n2>n8 and n2>n9 and n2>n10:
		maximo = n2
	elif n3>n1 and n3>n2 and n3>n4 and n3>n5 and n3>n6 and n3>n7 and n3>n8 and n3>n9 and n3>n10:
		maximo = n3
	elif n4>n1 and n4>n2 and n4>n3 and n4>n5 and n4>n6 and n4>n7 and n4>n8 and n4>n9 and n4>n10:
		maximo = n4
	elif n5>n1 and n5>n2 and n5>n3 and n5>n4 and n5>n6 and n5>n7 and n5>n8 and n5>n9 and n5>n10:
		maximo = n5
	elif n6>n1 and n6>n2 and n6>n3 and n6>n4 and n6>n5 and n6>n7 and n6>n8 and n6>n9 and n6>n10:
		maximo = n6
	elif n7>n1 and n7>n2 and n7>n3 and n7>n4 and n7>n5 and n7>n6 and n7>n8 and n7>n9 and n7>n10:
		maximo = n7
	elif n8>n1 and n8>n2 and n8>n3 and n8>n4 and n8>n5 and n8>n6 and n8>n7 and n8>n9 and n8>n10:
		maximo = n8
	elif n9>n1 and n9>n2 and n9>n3 and n9>n4 and n9>n5 and n9>n6 and n9>n7 and n9>n8 and n9>n10:
		maximo = n9
	else:
		maximo = n10

	print(f"El maximo es {maximo}.\n")

"""
# Con for

mayor = 0
maximo = 10 #Cantidad de numeros, puede variar
 
for mas_grande in range(maximo):
    num = int(input("Ingrese un numero:"))
    if num > mayor:
        mayor = num
 
print(f"El numero mayor es: {mayor}")