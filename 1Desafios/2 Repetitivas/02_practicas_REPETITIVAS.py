"""
print("Comienzo")
for i in range(3):
    print("Hola ", end="")
print("Final")

"""
"""
while True:
    op = input('Ingrese cualquier palabra, termina con FIN--> ')
    if op == 'FIN':
        break
    else:
        print(op)
print('Terminó la ejecución con FIN')
"""

"""
for letra in "Python":
    if letra == "h":
        break
print("Letra actual :", letra)
"""
"""
for letra in "Python":
    if letra == "h":
        continue
print("Letra actual :", letra)
"""

"""
---------------------------------------- DESAFÍO 1
Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.

a) *****Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al usuario la contraseña, 
y no le permita continuar hasta que la haya ingresado correctamente.*****

"""
"""
contrasena_fijada = "Prueba2022#"

print("Loguearse: ")

contrasena = input("Ingresar la contraseña fijada: ")

while contrasena!=contrasena_fijada:
	contrasena = input("Ingresar la contraseña fijada: ")
else:
	print("Contraseña correcta.")
"""
"""
b) *****Modificar el programa anterior para que solamente permita una cantidad fija de intentos. *****
"""
"""
contrasena_fijada = "Prueba2022#"

print("Loguearse: ")

contrasena_ingresada = input("Ingresar la contraseña fijada: ")

equivocaciones = 1
while contrasena_ingresada != contrasena_fijada:
    contrasena_ingresada = input("Ingresar la contraseña fijada: ")
    equivocaciones += 1
    if equivocaciones >= 3:
        print("Error. No puede realizar mas intentos.")
        break

else:
	print("Logueado correctamente.")
"""


