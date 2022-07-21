"""
Desafío 2	
Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, 
aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y 
la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero.
"""

print("\t*********************************************")
print("\tAprendamos sobre contaminacion en los mares.")
print("\t*********************************************\n")

factores_contaminantes = "aguas residuales", "sustancias químicas tóxicas", "aguas pluviales", "vertido de plásticos", "vertidos de petróleo", "actividad minera en alta mar", "cambio climático",

numero = int(input("Ingrese un numero: \n"))
numero_comparado = numero - 1
while numero_comparado > len(factores_contaminantes):
    print("Ingrese un numero más chico.")
    numero = int(input("Ingrese un numero: \n"))
    numero_comparado = numero - 1
else:
    print(factores_contaminantes[numero_comparado])
