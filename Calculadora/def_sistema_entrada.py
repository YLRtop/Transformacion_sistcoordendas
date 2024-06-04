

def dat_in():  # seleccion de sistema inicial


    print("1. Psad56")
    print("2. Sad69")
    print("3. Sirgas")
  

    opcion = int(input("\nElige un Sistema de coordenadas inicial:\n "))

    if opcion == 1:
        elipsoide = [6378388,6356911.946,(1/297),"Psad56"]  # psad56
    elif opcion == 2:
        elipsoide = [6378160,6356774.719,(1/298.25),"Sad69"] # sad69
    else:
        elipsoide = [6378137,6356752.314,(1/298.257223563),"Sirgas"]#sirgas  # wgs84 [6378137, 298.257223563, 6356752.31424518]
  
    return elipsoide

