"""
---------------------------------  Desafío 3
Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el 
cual debe existir en una cantidad de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL.
Escribir un programa que determine si es factible la utilización de fertilizantes.
"""


print("¡Mucho gusto! Vamos a determinar si es factible la utilización de fertilizantes.")
compuesto_utilizado = float(input("Determinar el porcentaje de compuesto por hectarea: "))
vegetacion = input("Que tipo de vegetacion existe en la hectarea: ")

if compuesto_utilizado>=10 and vegetacion.lower() != "Matorral":
    print("Es factible la utilización de fertilizantes.")
else:
    print("No es factible la utilización de fertilizantes.") 