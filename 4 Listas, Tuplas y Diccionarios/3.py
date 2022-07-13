"""
Desafío 3		
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). 
Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.
"""

print("\t**********************************")
print("\tDatos de contactos.")
print("\t**********************************\n")

crear_datos = str(input("Desea ingresar los datos de otro biologo?: "))
biologos_contactos = {}

while crear_datos.lower() == "si":
    while True:
        nombre = str(input("\nCual es su nombre?: \n"))
        if nombre not in biologos_contactos:
            break
        else:
            print("No puedes poner nombres iguales")

    mail = input("Escriba su email: \n")
    biologos_contactos[nombre] = mail

    crear_datos = str(input("\nDesea ingresar los datos de otro biologo?: "))

print(biologos_contactos)

    
