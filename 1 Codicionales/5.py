"""
---------------------------------  DESAFÍO 5
La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre del barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y 
los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.
"""

print("Mucho gusto, averiguaremos la seccion en la que se encuentra.")
print("Tipos de barrios: ")
print("centrico")
print("no centrico")

barrio = input("Ingresar el nombre del barrio en el que se encuentra: ")
ubicacion = input("Ingresar el tipo de barrio en el que se encuentra: ")
# Python ordena el abecedario de izquiera a derecha, es decir "A" es mayor a "M".

if ubicacion.lower() == "centrico" and barrio.lower()>="M":
    print("Seccion A.")
elif ubicacion.lower() == "no centrico" and barrio.lower()<="M":
    print("Seccion A.")
else:
    print("Seccion B.")