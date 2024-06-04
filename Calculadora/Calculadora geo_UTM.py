# -*- coding: utf-8 -*- 
"""
Created on Wed Sep  6 10:04:21 2023
"""
from def_sistema_entrada import dat_in  # elección del sistema inicial, guarda los parámetros del elipsoide
from def_convertir import conv  # Elección de transformación "de a"
from def_ingresocord_geo_2 import ingresocord  # ingreso de coordenadas
from def_GeoXYZ_OK2 import Geoxyz  # transformación de geodésicas a cartesianas sistema inicial
from def_para_XYZ import dat_out_para  # elección de parámetros de transformación 
from def_XYZ_Geo1 import XYZ_Geo  # transformación de coordenadas cartesianas a geodésicas modelo iterativo
from def_decimal_a_grd_min_seg import dec_gds  # transformación a sexagesimal
from def_pa_elip_out import pa_elip_out  # elipsoide de salida
from def_utm_geodesicas import utm_a_geodesicas
from def_geodesicas_utm import geo_a_utm
#import math as m


# Inicio de programa
while True:
    # Ingreso de coordenadas y sistema inicial
    print("********************************************************************")
    pa_elip = dat_in()
    print("\nParametros de elipsoide inicial", pa_elip[3], ":", "\na= ", pa_elip[0], "\nb= ", pa_elip[1], "\n ")
    print("********************************************************************")
    # Ingreso de tipo de transformación
    tran = conv()
    # Matriz de parámetros de salida
    elip_out = pa_elip_out(tran)
    print("\nParametros de elipsoide final", elip_out[3], ":", "\na= ", elip_out[0], "\nf= ", elip_out[1], "\n ")
    print("********************************************************************")
    # Ingreso de coordenadas
    coord_type = input("¿Qué tipo de coordenadas ingresará? (1. Geodésicas, 2. UTM): ")
    
    if coord_type == '1':
        mat_in = ingresocord()  # lat, long, hElip, Hso
    elif coord_type == '2':
        E = float(input("Ingrese la coordenada Este (E): "))
        N = float(input("Ingrese la coordenada Norte (N): "))
        huso = int(input("Ingrese el huso: "))
        hemisferio_in = input("Seleccione el hemisferio: (1. Norte, 2. Sur): ")
        if hemisferio_in == '1':
            hemisferio = "N"
        else:
            hemisferio = "S"
        geo_in= utm_a_geodesicas(pa_elip[0], pa_elip[1], E, N, huso, hemisferio)
        mat_in = [geo_in[0], geo_in[1], 0, huso]  # lat, long, hElip, Hso
    else:
        print("Opción no válida.")
        continue

    # Transformar de geodésicas a cartesianas
    mat_XYZ = Geoxyz(mat_in[0], mat_in[1], mat_in[2], pa_elip)  # lat, long, hElip, pa_elip
    print("\nMatriz coordenadas cartesianas XYZ de entrada: ", "\n", mat_XYZ, "\n ")
    print("\n*************************transformación*****************************\n")
    # Parámetros a utilizar
    matp_xyz = dat_out_para(mat_in, tran)  # matriz de parámetros de deltas XYZ
    res = mat_XYZ + matp_xyz
    # Resultado xyz a geodésicas
    res_geo = XYZ_Geo(res, elip_out)
    res_geo_gms = dec_gds(res_geo)
    
    #RESULTADO EN UTM
    
    UTM_FIN =geo_a_utm(res_geo[0], res_geo[1], elip_out, mat_in[4])
    
    
    print("\n******************************", elip_out[3],"**************************************")
    
    
    
  
    print("Coordenadas cartecianas de transformadas= \n", res )
    print("\n********************************************************************")
    print("\nCoordenadas geodésicas transformadas (decimal): ", "\n", "Latitud: ",res_geo[0],"°", "\n" ,
          "Longitud: ", res_geo[1],"°")
    print("\nCoordenadas geodésicas transformadas (gms): ", "\nLatitud: ", res_geo_gms[0][0],"°",
          res_geo_gms[0][1],"\'",res_geo_gms[0][2],"\'\'", "\nLongitud: ", res_geo_gms[1][0],"°",
                    res_geo_gms[1][1],"\'",res_geo_gms[1][2],"\'\'","\n ")
   
    print("\n********************************************************************")
    print("Coordenadas UTM= ", "\n" , "Este = ", UTM_FIN[0],"\n" , "Norte = ", UTM_FIN[1] )
    print("\n********************************************************************")
    # Preguntar al usuario si quiere realizar otra transformación
    continuar = input("\n ¿Desea realizar otra transformación? (s/n): \n ")
    if continuar.lower() != 's':
        print("\n Gracias por utilizar el programa. ¡Hasta luego!")
        break
