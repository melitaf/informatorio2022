"""
b. 	Haz un programa que almacene 5 elementos en una variable del tipo lista, 
la modiﬁque para que cada componente sea igual al cuadrado del componente original. 
El programa mostrara la lista resultante por pantalla.
"""
from stringprep import in_table_a1


print("\t########################")
print("\tListas modificadas:")
print("\t########################")
print()

lista_elem = []

contador_elem = 5
for elementos in range(contador_elem):
    elemento = float(input("Ingrese un valor a la lista: \n"))
    lista_elem.append(elemento**2)

print(lista_elem)


