
def funcion(*args):
    print(args)
    return print(sum(args))


tupla_numeros = []

numero = input("Ingrese un numero: \n")

while numero.isdigit():
    numero = float(numero)
    tupla_numeros.append(numero)
    numero = input("Ingrese un numero: \n")


funcion(*tupla_numeros)