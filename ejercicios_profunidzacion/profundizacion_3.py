# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con cadenas

"""
Enunciado:
Realice un programa que reciba por consola su nombre completo
e imprima en pantalla su nombre en los siguientes formatos:
- Todas las letras en minúsculas
- Todas las letras en mayúsculas
- Solo la primera letra del nombre en mayúscula

NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
de strings:
- lower : controla y devuelve toda la cadena sea toda en minuscula.
- upper : controla y devuelve toda la cadena sea toda en masyuscula.
- capitalize : Automaticamente hace que la primera letra se vuelva mayuscula. 

Puede buscar en internet como usar en Python estos métodos.
Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

Link de referencia:
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

Cualquier duda con estos métodos pueden consultarla por el campus
"""

print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio

print("Escriba su nombre completo")
nombre_completo = str(input())
string = nombre_completo

print("Escribalo de nuevo ")
nombre_completo2 = str(input())
c = nombre_completo2

print("Su nombre en minusculas es ",string.lower())
print("Su nombre en mayusculas es ",string.upper())
print("Su primer nombre comienza con la letra mayuscula",string[0].capitalize())

#Prueba con otra variable "c" y prueba del comando ".isspace()", ".isupper", ".islower" de tipo bool.
print("Su nombre esta en Minuscula ? ", c.islower())
print("Su nombre esta en Mayuscula ? ", c.isupper())
print("Uso espacios para escribir su nombre ? ",c.isspace())

print("Terminado!!! ")