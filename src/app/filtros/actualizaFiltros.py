import numpy as np
	
def actualizaFiltros():
	# Importa Matrices
	Y = np.load('app\static\datos\Y.npy')
	R = np.load('app\static\datos\R.npy')
	P_Modelos = np.load('app\static\datos\P_Modelos.npy')
	P_Mem_Users = np.load('app\static\datos\P_Mem_Users.npy')
	P_Mem_Juegos = np.load('app\static\datos\P_Mem_Juegos.npy')

	nJuegos,nUsers = Y.shape
	user = nUsers

	# Actuliza Y y R
	ceros = np.matrix(np.zeros(nJuegos))
	Y = np.concatenate((Y,ceros.T), axis=1)	
	R = np.concatenate((R,ceros.T), axis=1)	
	
	# Actuliza P_Modelos
	media = np.matrix(np.median(P_Modelos, axis=1))
	P_Modelos = np.concatenate((P_Modelos, media.T), axis=1)	
	
	# Actuliza P_Mem_Users
	media = np.matrix(np.median(P_Mem_Users, axis=1))
	P_Mem_Users = np.concatenate((P_Mem_Users, media.T), axis=1)
	
	# Actuliza P_Mem_Juegos
	#  Se actualiza utilizando la media por tiempo de ejecución
	#  En posteriores versiones estudiar actulización futura por filtro productos
	media = np.matrix(np.median(P_Mem_Juegos, axis=1))
	P_Mem_Juegos = np.concatenate((P_Mem_Juegos, media.T), axis=1)
	
	
	# Guarda tablas actualizadas
	np.save('app\static\datos\Y', Y)
	np.save('app\static\datos\R', R)
	np.save('app\static\datos\P_Modelos', P_Modelos)
	np.save('app\static\datos\P_Mem_Users', P_Mem_Users)
	np.save('app\static\datos\P_Mem_Juegos', P_Mem_Juegos)
	

