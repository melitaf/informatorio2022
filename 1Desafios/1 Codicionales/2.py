"""
---------------------------------  DESAFIO 2:
Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python
que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:
Tamaño Normal: Mensaje "Pez en buenas condiciones"
Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
Tamaño sobredimensionado: Mensaje "Pez contaminado"


"""
print ("Mucho gusto!!! Identifique el tamaño del pez, por favor!")

print ("A: Tamaño normal")
print ("B: Por debajo de lo normal")
print ("C: Un poco por encima de lo normal")
print ("D: Sobredimensionado")


tamaño_pez = input("Elija una de las opciones visualizadas (A, B, C, D): ")

if tamaño_pez.lower() == "a":
    print ("Pez en buenas condiciones!")
elif tamaño_pez.lower() == "b":
    print ("Pez con problemas de nutrición")
elif tamaño_pez.lower() == "c":
    print ("Pez con síntomas de organismo contaminado")
elif tamaño_pez.lower() == "d":
    print ("Pez contaminado")

while tamaño_pez.lower() > "d":
    
    tamaño_pez = input("Elija una de las opciones visualizadas (A, B, C, D): ")

    if tamaño_pez.lower() == "a":
        print ("Pez en buenas condiciones!")
    elif tamaño_pez.lower() == "b":
        print ("Pez con problemas de nutrición")
    elif tamaño_pez.lower() == "c":
        print ("Pez con síntomas de organismo contaminado")
    elif tamaño_pez.lower() == "d":
        print ("Pez contaminado")