# -*- coding: utf-8 -*-
"""
Filtro Colaborativo basodo en Usuarios
"""
import numpy as np

# Carga datos inicales - Matrices Y - R
Y = np.load('..\static\datos\Y.npy')
R = np.load('..\static\datos\R.npy')
nJuegos,nUsers = Y.shape

# Crea matriz similitud (Coef.Corr.Pearson)
sim = np.corrcoef(Y, rowvar=False)

# Crea matriz Predicción Filtro Colab. Usuarios
P_Mem_Users = np.copy(Y)

# Recorre todos los juegos sin Valoración para generar Predicción
# indices de juegos a Predecir rating
indPredecir = np.transpose(np.where(R==0))

for indP in indPredecir:

    juego = indP[0]
    user = indP[1]
    sumaDdo = 0
    sumaDsor = 0
	
    # Recorre todos los users que han jugado al juego y similutid > 0
    # indices de users que han jugado a juego a predecir para User
    indJugado = np.transpose(np.where(R[juego,:]==1))
    indJugado = indJugado[:,0]
    indJugadoRed = list(filter(lambda x: (sim[x,user]>0), indJugado))
	
    # Controla que no hay ningún usuario con sim > 0
    if len(indJugadoRed) > 0:
        for iUserJdo in indJugadoRed:
            sumaDdo = sumaDdo + (Y[juego,iUserJdo]-Y[:,iUserJdo].mean()) * sim[iUserJdo,user]
            sumaDsor = sumaDsor + np.absolute(sim[iUserJdo,user])
        P_Mem_Users[juego,user] = Y[:,user].mean() + (sumaDdo/sumaDsor)


# Guarda Matriz Pronosticos
np.save('../static/datos/P_Mem_Users', P_Mem_Users)
