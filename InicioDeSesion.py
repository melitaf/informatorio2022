"""
Escribir un programa que solicite el ingreso de un nombre de usuario.
Se debera verificar que se cumplan las siguientes condiciones:
- El nombre de usuario debe tener como minimo 8 caracteres y como maximo 15. Caso contrario, informar:
	"longitud minima es de 8 caracteres" si es que no se cumplio esta condicion;
	"longitud maxima es de 15 caracteres" si es que no se cumplio esta condicion.
- El nombre de usuario debe contener al menos 1 vocal en mayuscula. Caso contrario informar este error;
- El nombre de usuario debe contener al menos 1 caracter especial. Caso contrario informar este error.
Al final informa si el usuario ingresado es valido o no, de acuerdo a las reglas anteriormente mencionadas.
"""

print("Loguearse: ")

nombre_usuario = input("Escribir el nombre de usuario: ")

caracter_especial_cont = 0
caracter_especial = "!#$&%/()=?¡¿"

#Contador de caracteres especiales:

for x in nombre_usuario:
	for y in caracter_especial:
		if x == y:
			caracter_especial_cont = caracter_especial_cont + 1

#Cumplimentar requisitos:

if len(nombre_usuario)<8:
	print("Longitud minima es de 8 caracteres.")
elif len(nombre_usuario)>15:
	print("La longitud maxima son 15 caracteres.")
elif caracter_especial_cont<1:
	print("Ingrese un usuario con algun caracter especial.")
elif not nombre_usuario.islower():
	print("El nombre de usuario debe contener al menos 1 vocal en mayuscula")
elif not nombre_usuario.isupper():
	
else:
	print("Usuario valido.")

"""
 and not nombre_usuario.isnumeric() and not nombre_usuario.islower() and not nombre_usuario.isalpha() and not nombre_usuario.isupper() and caracter_especial_cont>1:
	print("Usuario correcto.")
else:
	print("Error: Ingresar minimo 8 y maximo 15 caracteres. Usted ingreso: ", len(nombre_usuario))

"""	

	



