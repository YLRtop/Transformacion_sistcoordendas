# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 09:04:47 2023

@author: Yerko
"""
#elegir el tipo de transformacion de coordenadas, entrega una opcion numerica
#la que ingresa 


def conv():
    print("1. De Sirgas a Psad56")
    print("2. De Sirgas a Sad69")
    print("3. De Psad56 a Sirgas")
    print("4. De Sad69 a Sirgas")

    opcion = int(input("\nElige una transformación de Sistema de coordenadas: \n"))

    if opcion == 1:
        trans = 1 
    elif opcion == 2:
        trans = 2
    elif opcion == 3:
        trans = 3 
    elif opcion == 4:
        trans = 4
    else:
        trans = None
        print("Opción no válida.")
 
    return trans



    
         
         
       