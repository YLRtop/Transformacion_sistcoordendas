# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 12:10:13 2023

@author: yleivar
"""

# bucle para calcualr la latitud de saldia utilizando una iteracion

import math as m #librerias de operaciones matematicas
import numpy as np #librerias de operaciones matematicas

#pa_elip = [6378137, 6356752.31424518]  # elipsoide grs-80, valores de a y b

#mat_XYZ = [1756025.55120742, -5025815.15556252, -3501691.52467817]
 # se debe utilizar los parametros del elipsoide de salida            
def XYZ_Geo(mat_XYZ, elip_out):
    a = elip_out[0]
    b = elip_out[1]  # b
    f=(a-b)/a # Achatamiento
    e2 = 2*f-f**2 # Excentricidad al cuadrado
    #e2=((2*f)-(f**2))

    r_XY = m.sqrt(mat_XYZ[0]**2 + mat_XYZ[1]**2)  # Distancia desde el eje Z

    # Latitud geocéntrica preliminar
    fi_p = m.atan2(mat_XYZ[2], r_XY * (1 - f))

    # umbral de convergencia
    condicion = np.radians(0.0001)  # 0.003086m (se ingresa en radianes)

    fi=np.radians(fi_p)  # Inicializar la latitud geodésica con el valor preliminar
    delta = 1  # Una diferencia inicial grande para iniciar el bucle
    itera = 0
    max_itera = 1000  # Establece un límite para evitar bucles infinitos
    
    
  #inicio de iteracion
    while delta > condicion and itera < max_itera:
        N = a / m.sqrt(1 - e2 * m.sin(fi)**2)
        h =r_XY / m.cos(fi) - N #altura elipsidal , datum de destino
        #ter_2=(1-((e2*N)/(N+fi)))**-1
        fi_nu =m.atan2(mat_XYZ[2] + e2 * N * m.sin(fi), r_XY)
        delta = abs(fi_nu - fi)  # Calcula la diferencia entre lat inicial y nueva salida
        fi = fi_nu
        itera += 1

    lambda_ = m.atan2(mat_XYZ[1], mat_XYZ[0])  #longuitud 

    mat_Geo = [m.degrees(fi), m.degrees(lambda_), h]
    print(f"Convergencia en iteration: {itera}")# se llama el resultado de iteracion

    return mat_Geo


