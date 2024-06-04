# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:20:36 2023

@author: yleivar
"""

#parametros de elipsoide de salida.

def pa_elip_out(tran):
     if tran ==1:
         elip_salida=[6378388,6356911.946,(1/297),"Psad56"]#psad56
     elif tran==2:
         elip_salida=[6378160,6356774.719,(1/298.25),"Sad69"]  # sad69
     else:
         elip_salida=[6378137,6356752.314,(1/298.257223563),"Sirgas"] #sirgas
     return elip_salida
         
