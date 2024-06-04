# -*- coding: utf-8 -*- 
"""Created on Wed Sep  6 10:04:21 2023 @author: yleivar"""
from def_sistema_entrada import dat_in # eleccion del sistema inicial , guarda los parametros del elipsoide
from def_convertir import conv #Eleccion de transformacion "desde  a"
from def_ingresocord_geo_2 import ingresocord #ingreso de coordenadas
from def_GeoXYZ_OK2 import Geoxyz # transformacion de geodesicas a cartecianas sistema inicial
from def_para_XYZ import dat_out_para #eleccion de parametros de transformacion 
from def_XYZ_Geo1 import XYZ_Geo # transformacion de coordenadas cartecianas a geodesicas modelo iterativo
from def_decimal_a_grd_min_seg import dec_gds #transformacion a sexaGecimal
from def_pa_elip_out import pa_elip_out #elipsoide de salida
#Inicio de programa
while True:
    # Ingreso de coordenadas y sistema inicial
    print("***********************|*********************************************")
    pa_elip = dat_in()
    print("\nParametros de elipsoide inicial", pa_elip[2],":", "\na= ",pa_elip[0],"\nf= ",pa_elip[1],"\n ")
    print("********************************************************************")
    # Ingreso de tipo de transformación
    tran = conv()
    #print(tran)
    # Matriz de parámetros de salida
    elip_out = pa_elip_out(tran)
    print("\nParametros de elipsoide final",elip_out[2],":", "\na= ",elip_out[0],"\nf= ",elip_out[1],"\n ")
    print("********************************************************************")
    # Ingreso de coordenadas
    mat_in = ingresocord()  # lat, long, hElip, Hso
    # Transformar de geodésicas a cartesianas
    mat_XYZ = Geoxyz(mat_in[0], mat_in[1], mat_in[2], pa_elip)  # lat, long, hElip, pa_elip
    print("\nMatriz coordenadas cartesianas XYZ de entrada: ", "\n", mat_XYZ,"\n ")
    print("\n*************************transformación*****************************\n")
    # Parámetros a utilizar
    matp_xyz = dat_out_para(mat_in, tran)  # matriz de parámetros de deltas XYZ
    res = mat_XYZ + matp_xyz
    # Resultado xyz a geodésicas
    res_geo = XYZ_Geo(res, elip_out)
    res_geo_gms = dec_gds(res_geo)
    print("\n********************************************************************")
    print("Coordenadas cartecianas de salida= ", res )
    print("\n********************************************************************")
    print("\nCoordenadas geodésicas transformadas (decimal): ", "\n", "Latitud: ",res_geo[0],"°", "\n" ,\
          "Longuitud: ", res_geo[1],"°" ,"Altura: ", res_geo[2],"\n")
    print("\nCoordenadas geodésicas transformadas (gms): ", "\nLatitud: ", res_geo_gms[0][0],"°",\
          res_geo_gms[0][1],"'",res_geo_gms[0][2],"''", "\nLongitud: ", res_geo_gms[1][0],"°",\
                    res_geo_gms[1][1],"'",res_geo_gms[1][2],"''","\n ")
    print("********************************************************************")
    # Preguntar al usuario si quiere realizar otra transformación
    continuar = input("\n ¿Desea realizar otra transformación? (s/n): \n ")
    if continuar.lower() != 's':
        print("\n Gracias por utilizar el programa. ¡Hasta luego!")
        break
