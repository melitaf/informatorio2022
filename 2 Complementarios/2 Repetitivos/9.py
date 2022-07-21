"""
9)Un censador recopila ciertos datos aplicando encuestas para el último Censo Nacional de Población y Vivienda. 
Desea obtener de todas las personas que alcance a encuestar en un día, que porcentaje tiene estudios de primaria,
 secundaria, carrera técnica, estudios profesionales y estudios de posgrado.
"""
# Resolviendo programa entendiendo que la consigna pide que cada encuestador agregue el total de sus numeros al programa (Y no 1x1),
# Y se va haciendo un total de encuestadores.

print("#############################")
print("Censo 2022.")
print("#############################\n")

# Iniciacion de variables requeridas:

censo_total = []
e_no_estudio = []
e_primaria = []
e_secundaria = []
e_tecnica = []
e_profesional = []
e_posgrado = []


# Contador de sujetos censados:

agregar_encuestador = str(input("Quiere agregar los numeros de un encuestador? (si // o para terminar ingresa cualquier letra): \n"))
print("Ingrese la cantidad de personas sensadas en cada categoria: \n")
while agregar_encuestador.lower() == "si":
    no_estudio = int(input("Cuantas personas no llegaron a estudiar?:\n"))
    primaria = int(input("Cuantas personas llegaron a estudiar solamente primaria?:\n"))
    secundaria = int(input("Cuantas personas llegaron a estudiar solamente secundaria?:\n"))
    tecnica = int(input("Cuantas personas llegaron a estudiar una carrera tecnica?:\n"))
    profesional = int(input("Cuantas personas llegaron a estudiar una profesion?:\n"))
    posgrado = int(input("Cuantas personas llegaron a estudiar un posgrado?:\n"))
    suma_encuestador = no_estudio + primaria + secundaria + tecnica + profesional + posgrado


    e_no_estudio.append(int(no_estudio))
    e_primaria.append(int(primaria))
    e_secundaria.append(int(secundaria))
    e_tecnica.append(int(tecnica))
    e_profesional.append(int(profesional))
    e_posgrado.append(int(posgrado))
    censo_total.append(int(suma_encuestador))

#A) Calculos para 1 solo sensista:
    print("Las estadisticas de este sensador son las siguientes:\n")
    print(f"La cantidad de personas sensadas por este encuestador es: {suma_encuestador}.")
    print(f"El porcentaje de personas que no llegaron a estudiar es {((int(no_estudio)/int(suma_encuestador))*100):.2f}% del total de individuos ingresador por este sensador.")
    print(f"El porcentaje de personas que llegaron a estudiar solamente primaria es {((int(primaria)/int(suma_encuestador))*100):.2f}% del total de individuos ingresador por este sensador.")
    print(f"El porcentaje de personas que llegaron a estudiar solamente secundaria es {((int(secundaria)/int(suma_encuestador))*100):.2f}% del total de individuos ingresador por este sensador.")
    print(f"El porcentaje de personas que llegaron a estudiar una tecnicatura es {((int(tecnica)/int(suma_encuestador))*100):.2f}% del total de individuos ingresador por este sensador.")
    print(f"El porcentaje de personas que llegaron a estudiar una profesion es {((int(profesional)/int(suma_encuestador))*100):.2f}% del total de individuos ingresador por este sensador.")
    print(f"El porcentaje de personas que llegaron a estudiar un posgrado es {((int(posgrado)/int(suma_encuestador))*100):.2f}% del total de individuos ingresador por este sensador.\n")

    print(e_no_estudio)
    print(e_primaria)
    print(e_secundaria)
    print(e_tecnica)
    print(e_profesional)
    print(e_posgrado)
    print(censo_total)

    agregar_encuestador = str(input("\nQuiere agregar los numeros de un encuestador? (si // o para terminar ingresa cualquier letra): \n"))

#B) Calculos de variables para todos los sensistas:

print("\nLas estadisticas totales del conjunto de censadores es:\n")
print(f"La cantidad de personas sensadas son: {sum(censo_total)}.")
print(f"El porcentaje total de personas que no llegaron a estudiar es {((sum(e_no_estudio)/sum(censo_total))*100):.2f}% en todo el senso.")
print(f"El porcentaje total de personas que llegaron a estudiar solamente primaria es {((sum(e_primaria)/sum(censo_total))*100):.2f}% en todo el senso.")
print(f"El porcentaje total de personas que llegaron a estudiar solamente secundaria es {((sum(e_secundaria)/sum(censo_total))*100):.2f}% en todo el senso.")
print(f"El porcentaje total de personas que llegaron a estudiar una tecnicatura es {((sum(e_tecnica)/sum(censo_total))*100):.2f}% en todo el senso.")
print(f"El porcentaje total de personas que llegaron a estudiar una profesion es {((sum(e_profesional)/sum(censo_total))*100):.2f}% en todo el senso.")
print(f"El porcentaje total de personas que llegaron a estudiar un posgrado es {((sum(e_posgrado)/sum(censo_total))*100):.2f}% en todo el senso.")

