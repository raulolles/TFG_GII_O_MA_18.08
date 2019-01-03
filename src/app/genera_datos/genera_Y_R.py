# -*- coding: utf-8 -*-
"""
Genera las Tablas Y R a partir de:
    - cantidad de juegos
    - 1000 usuarios ficticios con 100 valoraciones aleatorias por usuario

Matriz Y: ratings
Matriz X: juegos valorados
"""

import numpy as np
import random


ratingMax = 5
nUsers = 1000
nValoraciones = 100


# Genera valoraciones aleatorias entre 0 y 5
def generaTablas(nJuegos):
    
    # Crea Y R a zeros
    Y = np.zeros ((nJuegos, nUsers), dtype = np.float)
    R = np.zeros ((nJuegos, nUsers), dtype = np.int)
    
    # Rellena Y
    for user in range(nUsers):
        for j in range(nValoraciones):
            Y[random.randint(0,nJuegos-1), user] = random.randint(0, ratingMax)

    # Genera R
    R[Y>0]=1
    
    # Guarda Matrices
    np.save('../static/datos/Y', Y)
    np.save('../static/datos/R', R)
   
    
    