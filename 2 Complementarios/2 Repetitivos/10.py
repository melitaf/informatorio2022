"""
10) Mostrar los perímetros de varios triángulos ingresando sus lados por teclado, hasta que ya no desee.
"""


print("\t*******************")
print("\tTriangulos.")
print("\t*******************\n")


ingresar_triangulo = str(input("Desea ingresar un triangulo? ('s' ó 'cualquier otra letra para salir'): "))
while ingresar_triangulo != "s":
    print("Fin.")
    break
else:
    lado1 = float(input("\nIngrese el valor de 1 lado del triangulo: "))
    lado2 = float(input("\nIngrese el valor de 1 lado del triangulo: "))
    lado3 = float(input("\nIngrese el valor de 1 lado del triangulo: "))
    print(f"El perimetro del triangulo ingresado es de: {(lado1+lado2+lado3)}.")
    ingresar_triangulo = str(input("Desea ingresar un triangulo? ('s' ó 'cualquier otra letra para salir'): "))
