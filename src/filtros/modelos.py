# -*- coding: utf-8 -*-
"""
Filtro Colaborativo basado en Modelos
"""

import numpy as np
from scipy.optimize import minimize


# Calculo del Coste (J) y el Gradiante de J
def cofiCostFunc (parameters, Y, R, n_users, n_juegos, n_features, lamb):

    cost=0
    gradient=np.zeros_like(parameters)
    
    # Matriz X y Theta
    X = parameters[0 : n_juegos*n_features]
    X = X.reshape(n_juegos, n_features)
    Theta = parameters[n_juegos*n_features :]
    Theta = Theta.reshape(n_users, n_features)
    
    # Coste
    MatrizHipot = X.dot(Theta.T)
    MatrizError = (MatrizHipot - Y) * R
    MatrizErrorCuad = MatrizError ** 2
    MatrizErrorCuadPelVista = MatrizErrorCuad
    
    error = np.sum(MatrizErrorCuadPelVista)
    cost = error * 0.5
    
    # regularización
    cost = cost + np.sum(lamb*0.5*(X*X))
    cost = cost + np.sum(lamb*0.5*(Theta*Theta))
    
    # Gradiante
    gradX = MatrizError.dot(Theta) + lamb * X
    gradTheta = MatrizError.T.dot(X) + lamb * Theta
    gradient = np.append(gradX.flatten(), gradTheta.flatten())  
     
    return (cost, gradient)


# Define a function to be minimized
def cofiCostFunc_minimize(parameters):
    return cofiCostFunc(parameters,Y, R, nUsers, nJuegos, nFeat,lamb)


# Carga datos inicales - Matrices Y - R
Y = np.load('..\datos\Y.npy')
R = np.load('..\datos\R.npy')

nJuegos,nUsers = Y.shape
nFeat = 10
lamb = 10
max_iter=200
initParam = np.random.rand(1, nUsers*nFeat + nJuegos*nFeat)

# Minimize the function using minimize from the package scipy.optimize and get the optimized parameters
parameters = (minimize(cofiCostFunc_minimize,initParam,method="CG",jac=True,
                   options={'maxiter':max_iter, "disp":True})).x

                       
# Matriz X y Theta
X = parameters[0 : nJuegos*nFeat]
X = X.reshape(nJuegos, nFeat)
Theta = parameters[nJuegos*nFeat :]
Theta = Theta.reshape(nUsers, nFeat)

# Predicciones
P_Modelos = np.dot(X, Theta.T)

# Graba la matriz de predicción
np.save('../datos/P_Modelos', P_Modelos)
