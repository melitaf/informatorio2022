"""
Ejercicio 4: Mediana de tres valores

Escriba una función que tome tres números como parámetros y devuelva el valor medio de esos parámetros como resultado. 
Incluya un programa principal que lea tres valores del usuario y muestre su mediana.

Sugerencia: El valor medio es el medio de los tres valores cuando se ordenan en orden ascendente. 
Se puede encontrar usando declaraciones if, o con un poco de creatividad matemática.
"""

# Al referirnos a una mediana de 3 valores, nos aclara que es con un "n" impar. Además, la forma de calcular es de 
# Una mediana sin datos agrupados.

#Recordar que la Mediana podia ser: *** Con datos agrupados, con datos sin agrupar (par o impar).

print("\t***********************************")
print("\tEscribamos medianas.")
print("\t***********************************\n")

# Iniciacion de variables:
lista_mediana = []

agregar_num = str(input("Desea ingresar un numero? "))
while agregar_num.lower() == "si":
    numero = float(input("Ingrese el numero a calcular: "))
    lista_mediana.append(numero)
    lista_mediana.sort()
    print(lista_mediana)
    if (len(lista_mediana))%2 == 0:
        valor_medio = ((lista_mediana[((len(lista_mediana)-1)//2)]+lista_mediana[((len(lista_mediana))//2)])/2)
        print(valor_medio)
    else:
        valor_medio = lista_mediana[((len(lista_mediana)-1)//2)]
        print(valor_medio)

    agregar_num = str(input("Desea ingresar un numero? "))
