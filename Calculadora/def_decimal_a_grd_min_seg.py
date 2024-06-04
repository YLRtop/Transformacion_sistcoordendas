
def dec_gds(coordenadas):
    # Función auxiliar para convertir un solo valor
    def convertir(valor):
        grados = int(valor)
        minutos = int((valor - grados) * 60)
        segundos = (valor - grados - minutos / 60) * 3600
        return (grados, minutos, segundos)
    
    # Convertir latitud y longitud
    lat_grados, lat_minutos, lat_segundos = convertir(coordenadas[0])
    lon_grados, lon_minutos, lon_segundos = convertir(coordenadas[1])
    
    # Crear una matriz de 2x3 con los resultados
    matriz_gms = [[lat_grados, abs(lat_minutos), abs(lat_segundos)],
                  [lon_grados, abs(lon_minutos), abs(lon_segundos)]]
    return matriz_gms
