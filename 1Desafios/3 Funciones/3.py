"""
Desafío 3

Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades
 de Argentina durante la cuarentena. Luego la función debe devolver dos listas ordenadas. 
 La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.

"""
arboles_plantados = [101, 250, 52, 5, 85, 121, 301, 1, 6]
mas_de_100_arboles = []
menos_de_100_arboles = []

def separar(lista):
	for x in lista:
		if x < 100:
			menos_de_100_arboles.append(int(x))
		else:
			mas_de_100_arboles.append(int(x))
	return print(f"La cantidad de ciudades que plantaron mas de 100 arboles son: {len(mas_de_100_arboles)}.")
separar(arboles_plantados)
