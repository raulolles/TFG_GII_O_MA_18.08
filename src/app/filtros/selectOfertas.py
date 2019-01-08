import numpy as np
from pandas import read_table
import random


def selectDeMatriz(P,R,idUser,unidSelect,items):
	# Crea una matriz en la que se guardan los indices, R0 y P0
	P0= P[:,idUser]
	ind = range(0, len(R))
	l = np.concatenate((ind, R, P0))
	l = l.reshape(3, len(R))
	l = l.T

	# Selecciona valores y Ordena la matriz
	l = l[np.where(l[:,1] == 0)]  # deja en la matriz los juegos no jugados
	l = l[l[:,2].argsort()]       # ordena la matriz por P
	l = np.flipud(l)              # voltea la matriz para ofrecer en orden correcto

	seleccion = items.loc[l[:,0][0:unidSelect]].values.tolist()
	return seleccion
	
	
def importaTablas():

	# Importa Matrices
	Y = np.load('app\static\datos\Y.npy')
	R = np.load('app\static\datos\R.npy')
	P_Modelos = np.load('app\static\datos\P_Modelos.npy')
	P_Mem_Users = np.load('app\static\datos\P_Mem_Users.npy')
	P_Mem_Juegos = np.load('app\static\datos\P_Mem_Juegos.npy')
	
	# Importa Datos del scraping
	items = read_table('app\static\datos\datosJuegos.csv',header=None,sep=';',encoding='ISO-8859-1')
	items.columns = ['juego','fabricante','visitas', 'favoritos', 'comentarios', 'url']

	return Y, R, P_Modelos, P_Mem_Users, P_Mem_Juegos, items
	
	
def select(idUser):
	unidSelect = 5
	Y, R, P_Modelos, P_Mem_Users, P_Mem_Juegos, items = importaTablas()
	R0 = R[:,idUser]

	selectUsers = selectDeMatriz(P_Mem_Users,R0,idUser,unidSelect,items)	
	selectJuegos = selectDeMatriz(P_Mem_Juegos,R0,idUser,unidSelect,items)
	selectModelos = selectDeMatriz(P_Modelos,R0,idUser,unidSelect,items)

	return selectModelos, selectUsers, selectJuegos
	
def selectAleatorio():
	unidSelect = 5
	Y, R, P_Modelos, P_Mem_Users, P_Mem_Juegos, items = importaTablas()
	nJuegos,nUsers = Y.shape
	nJuegos = nJuegos-1
	select = list()
	
	for i in range (unidSelect):
		select.append(items.loc[random.randint(0,nJuegos)].values.tolist())
	
	return select