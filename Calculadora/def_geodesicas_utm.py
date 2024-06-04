# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 02:26:06 2024

@author: topoy
"""
import math as m


def geo_a_utm(latitud, longitud, elp_salida, hemi):
    k0=0.9996
    # Obtener los parámetros del elipsoide de salida
    pa_elip = elp_salida
    a = pa_elip[0]
    b = pa_elip[1]  
       
    # Segunda excentricidad
    e_prima = m.sqrt((a**2)-(b**2))/b
    
    print("e_prima= ",e_prima)
    
    # Segunda excentricidad al cuadrado
    e_prima2 = e_prima**2  
    print("e_prime2= ",e_prima2)
    
    #radio polar de curvatura
    c=(a**2)/b
    print("c= ", c)
        # Calcular huso y meridiano central del huso
    huso = int(longitud / 6 + 31)
    lambda_0 = huso * 6 - 183
    
    # transformar a radianes 
    lat_rad = m.radians(latitud)
    lon_rad = m.radians(longitud)
    lambda_0_rad = m.radians(lambda_0)
    print("lat_rad , lon_rad =",lat_rad, ",",lon_rad)
    # Calcular la distancia angular
    delta_lambda = lon_rad - lambda_0_rad

    # Calcular valores intermedios necesarios para la transformación
    
    #A
    A=m.cos(lat_rad)*m.sin(delta_lambda)
    #print("A= ",A)
        
    xi=(1/2)*m.log((1+A)/(1-A))
    #print("xi= ",xi)
    
    eta=m.atan(((m.tan(lat_rad))/(m.cos(delta_lambda))))-lat_rad
    #print("eta= ", eta)
    
    v = c / ((1 + e_prima2 * (m.cos(lat_rad)**2))**0.5) * k0 
    #print("v= ",v )
    
    zeta=(e_prima2/2)*xi**2*(m.cos(lat_rad)**2)
    #print("zeta= ",zeta )
    
    #Calcular A1, A2, J2, J4, J6
    A1 = m.sin(2 * lat_rad)
    A2 = A1 * m.cos(lat_rad)**2
    J2 = lat_rad + A1 / 2
    J4 = (3 * J2 + A2) / 4
    J6 = (5 * J4 + A2 * m.cos(lat_rad)**2) / 3
    
    #print("A1, A2, J2, J4, J6= ",A1,A2,J2,J4,J6)
   
    # Calcular alpha, beta, gamma
    alpha = (3 / 4) * e_prima2
    beta = (5 / 3) * alpha**2
    gamma = (35 / 27) * alpha**3
    #print("alfa, gamma, beta= ", alpha,beta, gamma )
   
    # Calcular Bm
    B0 = k0 * c * (lat_rad - alpha * J2 + beta * J4 - gamma * J6)
    #print("b0= ", B0)
    
    X=xi*v*(1+(zeta/3))+500000
    
    if hemi == "N":
        Y = eta * v * (1 + zeta) + B0
    else:
        Y = eta * v * (1 + zeta) + B0 + 10000000  # Sumar 10,000,000 si es hemisferio sur
    UTM_out=[X,Y]
    return UTM_out

'''pa_elip=[6378137,6356752.314,(1/298.257223563),"Sirgas"]
lat=-33.606177
lon=-70.571878
huso=19
hemi="S"

UTM_SALIDA=geo_a_utm(lat, lon, pa_elip, hemi)

print("ESTE SALIDA= ", UTM_SALIDA[0])

print("NORTE SALIDA= ", UTM_SALIDA[1])'''