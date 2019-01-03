# -*- coding: utf-8 -*-
"""
Filtro Colaborativo basodo en Productos
"""
import numpy as np

# Carga datos inicales - Matrices Y - R
Y = np.load('..\static\datos\Y.npy')
R = np.load('..\static\datos\R.npy')
nJuegos,nUsers = Y.shape

# Crea matriz similitud (Coef.Corr.Pearson)
sim = np.corrcoef(Y, rowvar=True)
# Da valor -1 a sim donde varianza de Y sea 0 (sin volores con NaN)   
sim[np.where(sim == np.NaN)] = -1

# Crea matriz Predicción Filtro Colab. Productos
P_Mem_Juegos = np.copy(Y)

# Recorre todos los juegos sin Valoración para generar Predicción
# indices de juegos [juego,usuario] a Predecir rating
indPredecir = np.transpose(np.where(R==0))

for indP in indPredecir:

    juego = indP[0]
    user = indP[1]
    
    #if (sim[:,juego]<=0).all is not None:
    # Indices a eliminar por sim negativa o ser el propio Juego
    indElim = np.array(np.where(sim[:,juego]<=0))
    indElim = np.append(indElim, juego)
    
    ratingUser = np.delete(Y[:,user], indElim)
    simJuego = np.delete(sim[:,juego], indElim)
    
    sumaDdo = np.sum(ratingUser * simJuego)
    sumaDsor = np.sum(np.absolute(simJuego))

    P_Mem_Juegos[juego,user] = sumaDdo/sumaDsor
	

# Guarda Matriz Pronosticos
np.save('../static/datos/P_Mem_Juegos', P_Mem_Juegos)