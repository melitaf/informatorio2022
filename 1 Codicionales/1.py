DESAFIO 1:
"""
En nuestro rol de Devs (Programador o Programadora de Software), debemos elaborar un programa en Python que
permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años que viene usando 
insecticida en su plantación. 
Si hace 10 o más añoss, debemos emitir el mensaje "Por favor solicite revisión de suelos en su plantación". 
Si hace menos de 10 años, debemos emitir el mensaje 
"Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación".
"""

print("Hola. Mucho gusto, ")
años_insecticida = int(input("Cuantos años hace que usa insecticida en sus plantaciones?: "))
if años_insecticida >= 10:
    print("Por favor solicite revision de sueles en sus plantaciones.")
else:
    print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación.")