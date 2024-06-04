# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:07:13 2023

@author: yleivar
"""

import math

def Geoxyz(lat, lon, h, pa_elip):
    a = pa_elip[0]  # Radio ecuatorial
    b = pa_elip[1]  # b
    f=(a-b)/a # Achatamiento
    e2 = f * (2 - f)  # Excentricidad al cuadrado

    # Conversión de latitud y longitud de grados decimales a radianes
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    # Cálculo de N y N prima (N2)
    N = a / math.sqrt(1 - e2 * math.sin(lat_rad)**2)
    N2 = N * (1 - e2)

    # Cálculo de las coordenadas cartesianas
    X = (N + h) * math.cos(lat_rad) * math.cos(lon_rad)
    Y = (N + h) * math.cos(lat_rad) * math.sin(lon_rad)
    Z = (N2 + h) * math.sin(lat_rad)

    return [X, Y, Z]
