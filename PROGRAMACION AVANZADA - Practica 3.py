#Disñe un segmento de codigo a partir del cual se
#geneneren lineas para los nombres de cada participante
#y otro segmento de codigo que contenga un móduo para entronctar
#si existe dentro de ese archivo algun participante con un nombre en particular.

#Agregar nombres

nombres = open ("myFilenombres.txt", "a")
a= 0
while a != "salir":
    a = input("Cual es tu nombre? (o 'salir' para terminar)")
    if a != "salir":
       line = nombres.write ("\n" + a)
nombres.close()

#Buscar nombres
#def buscar():
 #   buscar = open  ("myFilenombres.txt", "r")
    



