"""
DESAFÍO 5
Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura 
a la vía pública.
Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y 
un valor numérico de 5 dígitos a la Central con el siguiente significado:

3 letras: Correspondientes a la patente.
Del valor numérico:
	Los 3 primeros números corresponden a la patente
	El 4 número indica
		1- Tiró basura a la vía pública
		0 - No tiró basura a la vía pública

	El 5 número indica
		1- Ya había sido multado el vehículo
		0 - Vehículo sin multas.

Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y 
porcentaje de éstos que ya habían sido multados.
"""

print("\t=====================================")
print("\tInforme del Sistema de control de vehiculos 2015.")
print("\t=====================================\n")
# No debo hacer el sistema de control, solo los informes que surjan de ver el numero arrojado por el sistema.

#INICIACION DE VARIABLES: Contadores para utilizarlos al final en los calculos solicitados.
vehiculos_obs = 0
vehiculos_contaminantes = 0
vehiculos_multados = 0

introducir_num_control = str(input("Quiere ingresar un numero de control arrojado por el sistema?(Si o cualquier letra para salir: "))
while introducir_num_control.lower() == "si":
#Cantidad de vehiculos ingresados.
	num_control = input("Ingrese el numero de control arrojado por el sistema: \n").split()
#Al ingresar el split, el valor ingresado lo convierte en una lista iterable de string el cual es separado por los espacios en blanco. 
	vehiculos_obs += 1
#Cantidad de vehiculos contaminantes, se toma el valor del anteultimo elemento de la lista creada.
	digito4 = num_control[-2]
#Cantidad de vehiculos ya multados, se toma el valor del ultimo elemento de la lista creada.
	digito5 = num_control[-1]
#Conteo de vehiculos contaminados y multados.
	if digito4 == "1"and digito5=="1":
		vehiculos_contaminantes += 1
		vehiculos_multados += 1
	elif digito4 == "1" and digito5 != "1":
		vehiculos_contaminantes += 1
	else:
		pass

	introducir_num_control = str(input("Quiere ingresar un numero de control arrojado por el sistema?(Si o cualquier letra para salir: "))
else:
	print("Fin del informe.\n")

print(f"La cantidad de vehiculos observados por el sistema es de {vehiculos_obs}.")
print(f"La cantidad de vehiculos que han tirado basura es de {vehiculos_contaminantes}.")
print(f"El porcentaje de vehiculos que ya habian sido multados es de {((vehiculos_multados/vehiculos_contaminantes)*100):.2f}%.")

