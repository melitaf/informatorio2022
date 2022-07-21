"""
Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. 
Los sueldos deben ajustarse de la siguiente forma:
Sueldo Actual (en $)    Aumento

0 - 6000						15%

6000 - 7900					    10%

7900 - 12000				    6%

Más de 12000				    0%

Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, 
el sueldo actual y el sueldo aumentado.
"""
print("\t###########################")
print("\tSalarios 2022.")
print("\t###########################\n")

salario_actual = float(input("Ingrese su salario actual: \n$"))
if salario_actual > 12000:
    print("Su salario no está sujeto a aumento.")
elif salario_actual <= 12000 and salario_actual >7900:
    print("Le corresponde el 6% de aumento")
    aumento_salarial = salario_actual * 0.06
    print(("El aumento que le corresponde es de %s $")%(aumento_salarial))
    sueldo_aumentado = salario_actual + aumento_salarial
    print(("Su salario final es de %s $.")%(sueldo_aumentado))
elif salario_actual <= 7900 and salario_actual >6000:
    print("Le corresponde el 10% de aumento")
    aumento_salarial = salario_actual * 0.1
    print(("El aumento que le corresponde es de %s $")%(aumento_salarial))
    sueldo_aumentado = salario_actual + aumento_salarial
    print(("Su salario final es de %s $.")%(sueldo_aumentado))
elif salario_actual <= 6000 and salario_actual >0:
    print("Le corresponde el 15% de aumento")
    aumento_salarial = salario_actual * 0.15
    print(("El aumento que le corresponde es de %s $")%(aumento_salarial))
    sueldo_aumentado = salario_actual + aumento_salarial
    print(("Su salario final es de %s $.")%(sueldo_aumentado))


