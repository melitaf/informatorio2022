"""
Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.
"""

print("\t%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\tDivisores:")
print("\t%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

numero_n = float(input("Ingrese un numero: \n"))
numero_m = float(input("Ingrese un numero: \n"))

if numero_m % numero_n == 0:
    print(("El numero %s es divisor del numero %s.") % (numero_n, numero_m))