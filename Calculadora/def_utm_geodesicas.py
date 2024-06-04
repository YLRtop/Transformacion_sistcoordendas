import math as m


def utm_a_geodesicas(a, b, E, N, huso, hemi):
    k0=0.9996
    #exentricidad
    e=m.sqrt((a**2)-(b**2))/a
    #print("e= ",e) 
    
    # Segunda excentricidad
    e_prima = m.sqrt((a**2)-(b**2))/b
    
    #print("e_prima= ",e_prima)
    
    # Segunda excentricidad al cuadrado
    e_prima2 = e_prima**2  
    # print("e_prime2= ",e_prima2)
    
    #radio polar de curvatura
    c=(a**2)/b
    #print("c= ", c)
    
      # Calcular parámetros del elipsoide
    
    # Ajustar coordenadas UTM
    E -= 500000.0  # Eliminar retranqueo del eje de las X
    if hemi=="S":
        N -= 10000000.0        # Eliminar retranqueo del eje de las Y si es hemisferio sur
    #print("N,E RETRANQUEO= ",N,E)
    
    # meridiano central del huso
    lambda_0 = m.radians(huso * 6 - 183)
    #print ("lambda_0= ", lambda_0)
    
    # Calcular φ'
    phi_prima = N / (6366197.724 * k0)
    #print("phiprima= ", phi_prima)
    
    # Calcular v
    v = c / ((1 + e_prima2 * (m.cos(phi_prima)**2))**0.5) * k0
    #print("v= ",v)
    
    # Calcular a
    a_x = E / v
    #print("a_x= ",a_x)
    
    # Calcular A1, A2, J2, J4, J6
    A1 = m.sin(2 * phi_prima)
    A2 = A1 * m.cos(phi_prima)**2
    J2 = phi_prima + A1 / 2
    J4 = (3 * J2 + A2) / 4
    J6 = (5 * J4 + A2 * m.cos(phi_prima)**2) / 3
    #print("A1, A2, J2, J4, J6= ",A1,A2,J2,J4,J6)
    
    # Calcular alpha, beta, gamma
    alpha = (3 / 4) * e_prima2
    beta = (5 / 3) * alpha**2
    gamma = (35 / 27) * alpha**3
    #print("alfa, gamma, beta= ", alpha,beta, gamma )
    
    # Calcular Bm
    Bm = k0 * c * (phi_prima - alpha * J2 + beta * J4 - gamma * J6)
    #print("bm= ", Bm)
    
    # Cálculo de b2
    b2 = (N - Bm) / v
    # print("b2= ", b2)
    
    dzeta = ((e_prima2 * a_x**2) / 2) * m.cos(phi_prima)**2
    #print("dzeta=", dzeta)
    
    # Calcular ξ, η
    xi = a_x * (1 - (dzeta / 3))
    # print("xi=", xi)
    
    eta = b2 * (1 - dzeta) + phi_prima
    # print("eta= ",eta)
    
    # Calcular sen h
    sen_h = (m.e**xi - m.e**(-xi)) / 2
    #print("sen h= ", sen_h)
    
    # Calcular Δλ
    d_lamb = m.atan((sen_h / (m.cos(eta))))
    #print("d_lamb= ", d_lamb)
    
    # Calcular t
    t = m.atan(m.cos(d_lamb) * m.tan(eta))
    #print("t= ", t)
    # Calcular la latitud
    lat = phi_prima + (1 + e_prima2 * m.cos(phi_prima)**2 - (3 / 2) * e_prima2
    *m.sin(phi_prima) * m.cos(phi_prima) * (t - phi_prima)) * (t - phi_prima)

    # Calcular la longitud
    lon = d_lamb + lambda_0
    # Convertir a grados decimales
    lati = m.degrees(lat)
    long = m.degrees(lon)
        
    # Convertir a grados, minutos y segundos
    def decimal_a_gms(decimal):
        grados = int(decimal)
        minutos = int((decimal - grados) * 60)
        segundos = (decimal - grados - minutos / 60) * 3600
        return grados, minutos, segundos

    #lat_gms = decimal_a_gms(lati)
    #lon_gms = decimal_a_gms(long)
   # print("\n#####################################################\n latitud= ",lati,"\nLonguitud= ",long,
          #"\n#####################################################\n")
    coord_geo=[lati,long]
   
    return coord_geo

#Ejemplo de uso con valores de entrada
'''pa_elip=[6378388,6356911.946130]
N=4815453.640
E=435157.590
huso=30
hemi=N

lat, lon, lat_gms, lon_gms = utm_a_geodesicas(pa_elip[0], pa_elip[1], E, N, huso, hemi)

print(f"Latitud: {lat}° ({lat_gms[0]}° {lat_gms[1]}' {lat_gms[2]}\")")
print(f"Longitud: {lon}° ({lon_gms[0]}° {lon_gms[1]}' {lon_gms[2]}\")")
'''