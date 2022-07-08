"""
DESAFÍO 3
En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan a la caja y ofrecen tapitas para reciclar, 
de acuerdo a la cantidad que lleven en la caja le entregan un código de descuento que se aplicará sobre el total de su compra. Determinar la 
cantidad que pagara cada cliente desde que la tienda abre hasta que cierra. 
Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% y si es blanca no obtendrá descuento.

"""
print("Mucho gusto.")

# Iniciacion de variables:
# Entiendo que es la sumatoria de las tapitas que nos fueron dando durante el dia:
tapitas_acumuladas = []


# Entrada de datos):

while True:
	tapitas = input("Ingrese la cantidad de tapitas traida por el cliente: \n")

	if tapitas.lower() == "Cierre":
		break
	tapitas_acumuladas.append(int(tapitas))
	print(f"\nLa cantidad acumulada de tapitas es: {sum(tapitas_acumuladas)}.")

	media = sum(tapitas_acumuladas)/len(tapitas_acumuladas)
	print(f"La media del total es: {media}.\n")

# Determinacion de categorias (Como al enunciado le falta datos para determinar cuando es descuento rojo/amarillo/blanco):

print(sum(tapitas_acumuladas))




