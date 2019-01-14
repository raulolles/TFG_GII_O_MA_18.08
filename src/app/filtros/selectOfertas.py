import numpy as np
from pandas import read_table
import random

def calcula_estad_juego(juego,y,r):
	tabla_estad = list()
	
	y_juego = y[juego,:]
	users_jugado = np.sum(r[juego,:])
	puntuacion = np.sum(y_juego)
	puntuacion_media = puntuacion/users_jugado
	imagen_punt = imagen_puntuacion(puntuacion_media)
	
	tabla_estad.append(juego)
	tabla_estad.append(str("{:.1f}".format(puntuacion_media)))
	tabla_estad.append(imagen_punt)
	tabla_estad.append(users_jugado)
	
	y_jugados = y[juego,:]
	
	tabla_estad.append(len(np.where(y_juego ==5)[0]))
	tabla_estad.append(len(np.where(y_juego ==4)[0]))
	tabla_estad.append(len(np.where(y_juego ==3)[0]))
	tabla_estad.append(len(np.where(y_juego ==2)[0]))
	tabla_estad.append(len(np.where(y_juego ==1)[0]))

	return tabla_estad
	

def imagen_puntuacion(puntuacion):
	if puntuacion > -0.5 and puntuacion <= 0.5:
		str_imagen = "simbolos/star_cero.png"
	elif puntuacion < 1:
		str_imagen = "simbolos/star_cero_med.png"	
	elif puntuacion < 1.5:
		str_imagen = "simbolos/star_uno.png"	
	elif puntuacion < 2:
		str_imagen = "simbolos/star_uno_med.png"	
	elif puntuacion < 2.5:
		str_imagen = "simbolos/star_dos.png"
	elif puntuacion < 3:
		str_imagen = "simbolos/star_dos_med.png"
	elif puntuacion < 3.5:
		str_imagen = "simbolos/star_tres.png"
	elif puntuacion < 4:
		str_imagen = "simbolos/star_tres_med.png"
	elif puntuacion < 4.5:
		str_imagen = "simbolos/star_cuatro.png"
	elif puntuacion < 5:
		str_imagen = "simbolos/star_cuatro_med.png"
	else:
		str_imagen = "simbolos/star_cinco.png"
	
	return str_imagen

	
def select_de_matriz(y,p,r,id_user,unid_select,items):
	r0 = r[:,id_user]
	# Crea una matriz en la que se guardan los indices, R0 y P0
	p0= p[:,id_user]
	ind = range(0, len(r0))
	l = np.concatenate((ind, r0, p0))
	l = l.reshape(3, len(r0))
	l = l.T

	# Selecciona valores y Ordena la matriz
	l = l[np.where(l[:,1] == 0)]  # deja en la matriz los juegos no jugados
	l = l[l[:,2].argsort()]       # ordena la matriz por P
	l = np.flipud(l)              # voltea la matriz para ofrecer en orden correcto

	seleccion = list()
	linea_select_a = list()
	linea_select_b = list()
	
	for i in range (unid_select):
		juego = int(l[i][0])
		print (l)
		print(juego)
		linea_select_a = items.loc[juego].values.tolist()
		linea_select_b = calcula_estad_juego(juego,y,r)
		seleccion.append(linea_select_a + linea_select_b)
		
	return seleccion
	
	
def importa_tablas():
	# Importa Matrices
	y = np.load('app\static\datos\Y.npy')
	r = np.load('app\static\datos\R.npy')
	p_modelos = np.load('app\static\datos\P_Modelos.npy')
	p_mem_users = np.load('app\static\datos\P_Mem_Users.npy')
	p_mem_juegos = np.load('app\static\datos\P_Mem_Juegos.npy')
	
	# Importa Datos del scraping
	items = read_table('app\static\datos\datosJuegos.csv',header=None,sep=';',encoding='ISO-8859-1')
	items.columns = ['juego','fabricante','visitas', 'favoritos', 'comentarios', 'url']

	return y, r, p_modelos, p_mem_users, p_mem_juegos, items
	
	
def select_predicciones(id_user):
	unid_select = 5
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]

	select_users = select_de_matriz(y,p_mem_users,r,id_user,unid_select,items)	
	select_juegos = select_de_matriz(y,p_mem_juegos,r,id_user,unid_select,items)
	select_modelos = select_de_matriz(y,p_modelos,r,id_user,unid_select,items)

	return select_modelos, select_users, select_juegos
	
def select_aleatorio():
	unid_select = 5
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	n_juegos,n_users = y.shape
	n_juegos = n_juegos-1
	seleccion = list()
	linea_select_a = list()
	linea_select_b = list()
	
	for i in range (unid_select):
		juego = random.randint(0,n_juegos)
		linea_select_a = items.loc[juego].values.tolist()
		linea_select_b = calcula_estad_juego(juego,y,r)
		seleccion.append(linea_select_a + linea_select_b)
		
	return seleccion

def select_favoritos(id_user):
	unid_select = 5
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]
	
	# Crea una matriz en la que se guardan los indices, R0 y P0
	y0= y[:,id_user]
	ind = range(0, len(r0))
	l = np.concatenate((ind, r0, y0))
	l = l.reshape(3, len(r0))
	l = l.T

	# Selecciona valores y Ordena la matriz
	l = l[np.where(l[:,1] == 1)]  # deja en la matriz los juegos sí jugados
	l = l[l[:,2].argsort()]       # ordena la matriz por Y
	l = np.flipud(l)              # voltea la matriz para ofrecer en orden correcto

	seleccion = list()
	linea_select_a = list()
	linea_select_b = list()
	
	for i in range (unid_select):
		juego = int(l[i][0])
		print (l)
		print(juego)
		linea_select_a = items.loc[juego].values.tolist()
		linea_select_b = calcula_estad_juego(juego,y,r)
		seleccion.append(linea_select_a + linea_select_b)
		
	return seleccion