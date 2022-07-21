"""
---------------------------------------- DESAFÍO 2:
Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado de personas. 
Luego obtener estadísticas al respecto informando porcentaje de personas que han encontrado menos de 100 colillas, 
más de 100 y menos de 200, más de 200 colillas.

"""

print("Campana de recoleccion de colillas de cigarrillos 2022.")

#Iniciacion de variables:
recolectores = []
menosDe100 = 0
masDe100 = 0
masDe200 = 0

# Entrada de datos:

while True:
	colillas = input("Ingrese la cantidad de colillas recolectadas, y ponga 'fin' para terminar: \n")

	if colillas == "fin":
		break
	recolectores.append(int(colillas))

# Determinacion de categorias:
for persona in recolectores:
	if persona <= 100:
		menosDe100 += 1
	elif persona >100 and persona<200:
		masDe100 += 1
	elif persona >= 200:
		masDe200 += 1

# Visualizacion de estadisticas:

print("\n Las estadisticas de los recolectores es: ")
print(f"Los recolectores que recolectaron menos de 100 colillas tienen un {(menosDe100/len(recolectores)*100):.2f}% del total recolectado. \n")
print(f"Los recolectores que recolectaron menos de 100 colillas tienen un {(masDe100/len(recolectores)*100):.2f}% del total recolectado. \n")
print(f"Los recolectores que recolectaron menos de 100 colillas tienen un {(masDe200/len(recolectores)*100):.2f}% del total recolectado. \n")