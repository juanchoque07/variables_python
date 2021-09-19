# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados

#Recortes
parte_1 = palabra_1[0:3]
parte_2 = palabra_2[0:2]
#Union
nueva_palabra =(parte_1+parte_2)
#Muestra
print("Las primeras 3 letras de", palabra_1,"son",parte_1)
print("Las primeras 2 letras de", palabra_2,"son",parte_2)

print("La nueva palabra formada es",nueva_palabra)