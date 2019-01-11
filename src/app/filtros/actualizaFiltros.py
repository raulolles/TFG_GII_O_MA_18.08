import numpy as np
	
def actualiza_filtros():
	# Importa Matrices
	Y = np.load('app\static\datos\Y.npy')
	R = np.load('app\static\datos\R.npy')
	p_modelos = np.load('app\static\datos\P_Modelos.npy')
	p_mem_users = np.load('app\static\datos\P_Mem_Users.npy')
	p_mem_juegos = np.load('app\static\datos\P_Mem_Juegos.npy')

	n_juegos,n_users = Y.shape

	# Actuliza Y y R
	ceros = np.matrix(np.zeros(n_juegos))
	Y = np.concatenate((Y,ceros.T), axis=1)	
	R = np.concatenate((R,ceros.T), axis=1)	
	
	# Actuliza P_Modelos
	media = np.matrix(np.median(p_modelos, axis=1))
	p_modelos = np.concatenate((p_modelos, media.T), axis=1)	
	
	# Actuliza P_Mem_Users
	media = np.matrix(np.median(p_mem_users, axis=1))
	p_mem_users = np.concatenate((p_mem_users, media.T), axis=1)
	
	# Actuliza P_Mem_Juegos
	#  Se actualiza utilizando la media por tiempo de ejecución
	#  En posteriores versiones estudiar actulización futura por filtro productos
	media = np.matrix(np.median(p_mem_juegos, axis=1))
	p_mem_juegos = np.concatenate((p_mem_juegos, media.T), axis=1)
	
	
	# Guarda tablas actualizadas
	np.save('app\static\datos\Y', Y)
	np.save('app\static\datos\R', R)
	np.save('app\static\datos\P_Modelos', p_modelos)
	np.save('app\static\datos\P_Mem_Users', p_mem_users)
	np.save('app\static\datos\P_Mem_Juegos', p_mem_juegos)
	

