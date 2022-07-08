"""
Desafío 1
150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 
Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o 
chicle, e imprima la cantidad de años que tarda en degradarse.
"""

def degradacion():

	print("\t##################")
	print("\tLos elementos contaminantes son:")
	print("\t##################\n")	
	
	print("1) Bolsa de plastico")
	print("2) Botellas pet")
	print("3) Envase de tetrabrik")
	print("4) Chicle")

	elemento = input("Ingrese el elemento encontrado: \n")

	bolsa = "Las bolsas de plastico comunes, tardan 150 años en degradarse."
	botella_pet = "Las botellas pet tardan 1000 años en degradarse."
	tetrabrik = "El envase de tetrabrik tarda 30 años en degradarse."
	chicle = "Los chicles tardan 5 años en degradarse."

	if elemento == "1":
		print(bolsa)
	elif elemento == "2":
		print(botella_pet)
	elif elemento == "3":
		print(tetrabrik) 
	elif elemento == "4": 
		print(chicle) 

	return elemento

degradacion()
