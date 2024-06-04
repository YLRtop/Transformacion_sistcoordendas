import numpy as np

def dat_out_para(mat_in,tran): #transformacion final
   
    ############################ valores de transformacion 
         
    #opcion 1
    # de sirgas a psad56
   
    sir_psad1= np.array([302,-272,360])#lat 17.5 a 26
    sir_psad2= np.array([328,-340,329])#lat 26 a 36
    sir_psad3= np.array([352,-403,287])#lat 36 a 44
    
    #opcion 2
    # de sirgas a sad69
    sir_sad1 = np.array([59,11,52])#lat 17.5 a 32
    sir_sad2 = np.array([64,0,32])#lat 32 a 36
    sir_sad3 = np.array([72,-10,32])#lat 36 a 44
    sir_sad4 = np.array([79,-13,14])#lar 44 al sur
    
    
    #opcion 3
    # de  psad56 a sirgas 
   
    psad_sir1= np.array([-302,272,-360])#lat 17.5 a 26
    psad_sir2= np.array([-328,340,-329])#lat 26 a 36
    psad_sir3= np.array([-352,403,-287])#lat 36 a 44
    
    #opcion 4
    # de sad69 a sirgas 
    sad_sir1 = np.array([-59,-11,-52])#lat 17.5 a 32
    sad_sir2 = np.array([-64,0,-32])#lat 32 a 36
    sad_sir3 = np.array([-72,10,-32])#lat 36 a 44
    sad_sir4 = np.array([-79,13,-14])#lar 44 al sur
    

    # guardar en mat_para parametros de transformacion segun latitud
        
  #caso 1 de sirgas a psad56
  
    if tran == 1:
        if abs(mat_in[0]) >17.5 and abs(mat_in[0])<=26:
            mat_para=sir_psad1 #matriz de parametros segun la latitud
        elif abs(mat_in[0])>26 and abs(mat_in[0])<=36:
            mat_para=sir_psad2 #matriz de parametros segun la latitud
        else:
            mat_para=sir_psad3
        return mat_para
    
   #caso 2 de sirgas a sad69
   
    elif tran==2:
 
        if abs(mat_in[0])>17.5 and abs(mat_in[0]) <= 32:
            mat_para=sir_sad1 #matriz de parametros segun la latitud
        elif abs(mat_in[0])>32 and abs(mat_in[0])<=36:
            mat_para=sir_sad2 #matriz de parametros segun la latitud
        elif abs(mat_in[0])>36 and abs(mat_in[0])<=44:
            mat_para=sir_sad3 #matriz de parametros segun la latitud
        else:
            mat_para=sir_sad4 #matriz de parametros segun la latitud
        return mat_para
    
    
    #caso 3 de  psad56 a sirgas
    
    elif tran == 3:
        if abs(mat_in[0]) >17.5 and abs(mat_in[0])<=26:
            mat_para=psad_sir1 #matriz de parametros segun la latitud
        elif abs(mat_in[0])>26 and abs(mat_in[0])<=36:
            mat_para=psad_sir2 #matriz de parametros segun la latitud
        else:
            mat_para=psad_sir3
        return mat_para
    
    #caso 4 de sad69 a sirgas 
    
    else:
  
         if abs(mat_in[0])>17.5 and abs(mat_in[0]) <= 32:
             mat_para=sad_sir1 #matriz de parametros segun la latitud
         elif abs(mat_in[0])>32 and abs(mat_in[0])<=36:
             mat_para=sad_sir2 #matriz de parametros segun la latitud
         elif abs(mat_in[0])>36 and abs(mat_in[0])<=44:
             mat_para=sad_sir3 #matriz de parametros segun la latitud
         else:
             mat_para=sad_sir4 #matriz de parametros segun la latitud
         return mat_para
    print("###################################################################\n Parametros elegidos= ",mat_para)
    return mat_para 

 
  

       
    
