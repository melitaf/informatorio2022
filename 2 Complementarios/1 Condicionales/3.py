#Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.

print("\t=======================")
print("\tDeterminemos que numero es mayor.")
print("\t=======================\n")

lista_num = []

contador_conj = 3
for conjunto in range(contador_conj):
    numero = int(input("Ingrese un numero de 3 digitos: "))
    lista_num.append(numero)

print(lista_num)

if lista_num[0]<lista_num[1] and lista_num[0]<lista_num[2]:
    print("Es correcto.")
