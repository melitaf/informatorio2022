"""
Desafío 1
Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, 
almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. 
"""

print("\t=====================")
print("\tInforme de conocimiento de Contaminacion.")
print("\t=====================\n")

#Iniciacion de valores:
contaminacion_encuestas = []


conocimiento_contaminacion = str(input("Agregar persona encuestada: \n"))
while conocimiento_contaminacion.lower() == "si":
    valor_conocimiento = int(input("Ingrese cuanto conoce de contaminacion(del 1 al 10): "))
    contaminacion_encuestas.append(valor_conocimiento)
    conocimiento_contaminacion = str(input("Agregar persona encuestada: \n"))
    contaminacion_encuestas.sort()

print(contaminacion_encuestas)
