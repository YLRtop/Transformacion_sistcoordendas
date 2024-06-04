# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 16:48:04 2023

@author: Yerko
"""

def ingresocord():

          
    # Mostrar opciones
    print("Elige una opción: \n")
    print("1. Ingreso de coordenadas iniciales sexagecimal\n")
    print("2. Ingreso de coordenadas iniciales sexadecimal\n")
    
    # Solicitar al usuario que elija el tipo de notación
    tipo = input("¿En qué notación desea ingresar las coordenadas?\n  ")
    
    if tipo == "1":
        # Lista para almacenar las coordenadas convertidas y otros datos
        mat_in = []

        # Solicitar al usuario las coordenadas y la altura
        lat = input("Ingresa latitud en grados, minutos y segundos separado por un espacio:\n  ")
        lon = input("Ingresa longitud en grados, minutos y segundos separado por un espacio:\n  ")
        h =float(0)
        
        #solicitud de hemisferio
        print("\nElige un hemisferio Norte o Sur: \n")
        print("1.Norte\n")
        print("2.Sur\n")
        hemi_in=input("Selecciona hemisferio:\n  ")
        if hemi_in=="1"   :
            hemisferio="N"
        else:
            hemisferio="S"
        # Dividir la entrada en elementos, ya que entran separadas por espacio
        lat_ = lat.split()
        lon_ = lon.split()

        # Manejar el signo para la latitud
        sign_lat = -1 if float(lat_[0]) < 0 else 1
        # Convertir a grados decimales manteniendo el signo
        lat_deg = sign_lat * (abs(float(lat_[0])) + (float(lat_[1]) / 60) + (float(lat_[2]) / 3600))

        # Manejar el signo para la longitud
        sign_lon = -1 if float(lon_[0]) < 0 else 1
        # Convertir a grados decimales manteniendo el signo
        lon_deg = sign_lon * (abs(float(lon_[0])) + (float(lon_[1]) / 60) + (float(lon_[2]) / 3600))
        
        # Calcular el huso horario
        Hso = int((lon_deg / 6) + 31)
        
        # Agregar los datos convertidos a la lista
        mat_in.append(lat_deg)
        mat_in.append(lon_deg)
        mat_in.append(h)
        mat_in.append(Hso)
        mat_in.append(hemisferio)
        return mat_in 
    else:
        
        
        # Lista para almacenar las coordenadas convertidas y otros datos
        mat_in = []

        # Solicitar al usuario las coordenadas y la altura en formato sexadecimal
        ingreso = input('\nIngresa coordenadas geodésicas (sexadecimal) iniciales separadas por espacio y en orden Lat, Long : ')
        datos = ingreso.split()
        
        #solicitud de hemisferio
        print("\nElige un hemisferio Norte o Sur: \n")
        print("1.Norte\n")
        print("2.Sur\n")
        hemi_in=input("Selecciona hemisferio:\n  ")
        if hemi_in=="1":
            hemisferio="N"
        else: 
            hemisferio="S"

        # Convertir los datos de entrada a flotantes
        lat = float(datos[0])
        lon = float(datos[1])
        hElip = float(0)

        # Calcular el huso horario
        Hso = int((lon / 6) + 31)
    
        # Agregar los datos convertidos a la lista
        mat_in.append(lat)
        mat_in.append(lon)
        mat_in.append(hElip)
        mat_in.append(Hso)
        mat_in.append(hemisferio)

        return mat_in

# prueba de la función y mostrar el resultado
#entrada = ingresocord()
#print(entrada)


