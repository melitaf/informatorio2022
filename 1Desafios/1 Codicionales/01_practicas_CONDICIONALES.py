#print ("Hola Mundo")

"""
la sangría en Python es muy importante.

Python usa sangría para indicar un bloque de código
Establecer una sangría se denomina IDENTAR O IDENTACIÓN.

(PARA INSERTAR COMENTARIOS, USAMOS:
numeral...Para 1 sola linea;
triple comillas... Para englobar un texto, poniendo al principio y al final del texto)
"""
"""
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
"""

"""
Normalmente, cuando crea una variable dentro de una función, esa variable es LOCAL y solo se puede usar dentro de esa función.

Para crear una variable global dentro de una función, puede usar la "global" palabra clave.
"""
### FORMAS DE PONER LOS DIAS DE LA SEMANA:
                                        # PRIMERA FORMA, utilizando if y else:
"""
dia_semana = int(input("Ingrese un numero: "))
dia = None

if dia_semana == 1:
    dia = "Lunes"
else:
    if dia_semana ==2:
        dia = "Martes"
    else:
        if dia_semana == 3:
            dia = "Miercoles"
        else:
            if dia_semana == 4:
                dia = "Jueves"
            else:
                if dia_semana == 5:
                    dia = "Viernes"
                else:
                    if dia_semana == 6:
                        dia = "Sabado" 
                    else:
                        if dia_semana == 7:
                            dia = "Domingo"

if dia is None:
  print ("El numero asignado esta fuera del rango del 1 al 7.")
else:
  print("El dia de la semana es: ", dia) 
  """

                                        # SEGUNDA FORMA, utilizando elif:
"""                                       
dia_semana = int(input("Ingrese un numero: "))
dia = None

if dia_semana == 1:
    dia = "Lunes"
elif dia_semana ==2:
      dia = "Martes"
elif dia_semana == 3:
      dia = "Miercoles"
elif dia_semana == 4:
      dia = "Jueves"
elif dia_semana == 5:
      dia = "Viernes"
elif dia_semana == 6:
      dia = "Sabado" 
elif dia_semana == 7:
      dia = "Domingo"
else:
    print ("No ingreso ningun numero valido")

if dia is None:
  print ("El numero asignado esta fuera del rango del 1 al 7.")
else:
  print("El dia de la semana es: ", dia)
"""



                                        # TERCERA FORMA, comparando listas:
"""
DIAS_DE_LA_SEMANA = [" ", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
numero_de_dia = [1, 2, 3, 4, 5, 6, 7]



"""
"""
EJERCICIO 1:
Un local vende ropa al por menor y mayor. Si la compra es por una cantidad igual a 10 remeras, el precio por unidad es de tan solo del 80%.
Preguntar cuantas unidades de remeras se incluyen en la compra y el precio por unidad.
Devolver el precio total de la compra.

"""
"""
print("Buen día")
Q = int(input("Ingrese la cantidad vendida: "))
P = float(input("Ingrese el precio: "))

if Q>= 10:
    print("El monto a cobras es: ", Q*(P*0.8))
else:
    print("El monto a cobras es: ", Q*P)

print("Muchas gracias")
"""
"""
EJERCICIO 2:
Ingresar la edad de una persona, indicando/mostrando si es menor de edad o mayor.
"""
"""
print("Hola, mucho gusto.")
edad = int(input("Ingresar su edad: "))
if edad < 18:
    print("Es menor de edad.")
else:
    print("Es mayor de edad.")
"""
"""
EJERCICIO DE CLASE:
Se debe hacer un programa que nos calcule cuanto dinero se desembolsaria en una compra. Sabiendo que si el importe sumado es superior a $1500 se aplica el 30% de descuento.
Si es superior a $1000 se aplica el 20%. Y si es superior a $750 solo el 10%.

"""
"""
Monto = float(input("Ingrese el monto total sujeto a descuento: "))
if Monto >= 1500:
    print("El descuento aplicado es del 30%")
    Monto_a_Cobrar=Monto * (1-0.3)
    print("El total a cobrar es: $", Monto_a_Cobrar)
elif Monto>=1000:
    print("El descuento aplicado es del 20%")
    Monto_a_Cobrar=Monto * (1-0.2)
    print("El total a cobrar es: $", Monto_a_Cobrar)
elif Monto>=750:
    print("El descuento aplicado es del 10%")
    Monto_a_Cobrar=Monto * (1-0.1)
    print("El total a cobrar es: $", Monto_a_Cobrar)
else:
    print("No se aplica descuento.")
    Monto_a_Cobrar=Monto * 1
    print("El total a cobrar es: $", Monto_a_Cobrar)

"""

### DESAFIOS EJERCICIOS CONDICIONALES EJEMPLOS:
""" DESAFIO 1:
Se necesita calcular el resultado final de un cuestionario realizado por una persona.
Solicita cantidad total de preguntas y luego cantidad de respuestas correctas.
Si el porcentaje de respuestas correctas es mayor o igual a 90, el resultado es EXCELENTE. 
Si el porcentaje de respuestas correctas es mayor o igual a 70, el resultado es BUENO. 
Si el porcentaje de respuestas correctas es mayor o igual a 60, el resultado es APROBADO. 
Si el porcentaje de respuestas correctas es menor a 60, el resultado es NO ALCANZÓ.  
"""
"""
q_preguntas = int(input("Ingrese la cantidad de preguntas realizadas: "))
q_respuestas = int(input("Ingrese la cantidad de respuestas correctas: "))

resultado = (q_respuestas/q_preguntas)*100

if resultado >= 90:
    print("El resultado final obtenido es EXCELENTE, su puntaje es: ", resultado)
elif resultado >=70:
    print("El resultado final obtenido es BUENO, su puntaje es: ", resultado)
elif resultado >= 60:
    print("El resultado final obtenido es APROBADO, su puntaje es: ", resultado)
else:
    print("El resultado final obtenido NO ALCANZO, su puntaje es: ", resultado)

"""
"""
Actividad DE LA CLASE:
Los alumnos de un curso se han dividido en 2 grupos, A y B. De acuerdo al nombre y al sexo.
El grupo A, esta formado por las mujeres con un nombre anterior a la M y hombres con un nombre posterior a la N.
El grupo B, por el resto. Escribir un programa que pregunte al usuario el nombre y el sexo, y muestre por pantalla el grupo que le corresponde.
"""
"""
print("Hola. Mucho gusto, vamos a asignarle el grupo al que pertenece.")

nombre_alumnos= input("Ingrese su nombre: ")
nombre_alumnos_lower = nombre_alumnos.lower()

sexo_alumnos= input("Ingrese su sexo (F/M): ")
#ACA PODRIAMOS AGREGAR UN WHILE PARA QUE EN EL CASO DE QUE LA PERSONA INGRESE VALORES DISTINTOS A "F" ó "M", ME REPITA EL BUCLE HASTA QUE INGRESE CORRECTAMENTE.

sexo_alumnos_upper = sexo_alumnos.upper()
print(sexo_alumnos_upper)

if sexo_alumnos_upper == "F" and nombre_alumnos_lower < "m":
    print("La persona pertenece al grupo A")
elif sexo_alumnos_upper == "M" and nombre_alumnos_lower > "n":
    print("La persona pertenece al grupo A")
else:
    print("La persona pertenece al grupo B")
"""

