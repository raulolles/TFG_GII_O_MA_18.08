import numpy as np
import pandas as pd
from pandas import read_table
import random
import jellyfish as jel

def calcula_estad_juego(juego,y,r):
	tabla_estad = list()
	
	y_juego = y[juego,:]
	users_jugado = np.sum(r[juego,:])
	puntuacion = np.sum(y_juego)
	puntuacion_media = puntuacion/users_jugado
	imagen_punt = imagen_puntuacion(puntuacion_media)
	
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
	if puntuacion > -0.5 and puntuacion <= 0.4:
		str_imagen = "simbolos/star_cero.png"
	elif puntuacion < 1:
		str_imagen = "simbolos/star_cero_med.png"	
	elif puntuacion < 1.4:
		str_imagen = "simbolos/star_uno.png"	
	elif puntuacion < 2:
		str_imagen = "simbolos/star_uno_med.png"	
	elif puntuacion < 2.4:
		str_imagen = "simbolos/star_dos.png"
	elif puntuacion < 3:
		str_imagen = "simbolos/star_dos_med.png"
	elif puntuacion < 3.4:
		str_imagen = "simbolos/star_tres.png"
	elif puntuacion < 4:
		str_imagen = "simbolos/star_tres_med.png"
	elif puntuacion < 4.4:
		str_imagen = "simbolos/star_cuatro.png"
	elif puntuacion < 5:
		str_imagen = "simbolos/star_cuatro_med.png"
	else:
		str_imagen = "simbolos/star_cinco.png"
	
	return str_imagen

	
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

	seleccion = ejecuta_seleccion (id_user, l, items, y, r, unid_select)
		
	return seleccion
	
	
def select_predicciones(id_user):
	unid_select = 6
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]

	select_users = select_de_matriz(y,p_mem_users,r,id_user,unid_select,items)	
	select_juegos = select_de_matriz(y,p_mem_juegos,r,id_user,unid_select,items)
	select_modelos = select_de_matriz(y,p_modelos,r,id_user,unid_select,items)

	return select_modelos, select_users, select_juegos

	
def select_aleatorio():
	unid_select = 6
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
	unid_select = 100
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

	seleccion = ejecuta_seleccion (id_user, l, items, y, r, unid_select)
		
	return seleccion

	
def select_mas_jugados(id_user, jugado):
	unid_select = 100
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]
	
	# Crea una matriz en la que se guardan los indices, R0 y suma juegos
	veces_jug = r.sum(axis = 1)
	ind = range(0, len(r0))
	l = np.concatenate((ind, r0, veces_jug))
	l = l.reshape(3, len(r0))
	l = l.T
	
	# Ordena la matriz
	if jugado == 0:
		l = l[np.where(l[:,1] == 0)]  # deja en la matriz los juegos no jugados
	elif jugado == 1:
		l = l[np.where(l[:,1] == 1)]  # deja en la matriz los juegos si jugados

	l = l[l[:,2].argsort()]
	l = np.flipud(l)
	
	seleccion = ejecuta_seleccion (id_user, l, items, y, r, unid_select)
	
	return seleccion

	
def select_mejor_valorados(id_user, jugado):
	unid_select = 100
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]
	
	# Crea una matriz en la que se guardan los indices, R0 y suma juegos
	valor_medio = y.sum(axis = 1) / r.sum(axis = 1)
	valor_medio[np.where(np.isnan(valor_medio))] = 0

	ind = range(0, len(r0))
	l = np.concatenate((ind, r0, valor_medio))
	l = l.reshape(3, len(r0))
	l = l.T
	
	# Ordena la matriz
	if jugado == 0:
		l = l[np.where(l[:,1] == 0)]  # deja en la matriz los juegos no jugados
	elif jugado == 1:
		l = l[np.where(l[:,1] == 1)]  # deja en la matriz los juegos si jugados
		
	l = l[l[:,2].argsort()]
	l = np.flipud(l)
	
	seleccion = ejecuta_seleccion (id_user, l, items, y, r, unid_select)
		
	return seleccion


def select_archive(id_user,columna,jugado):
	unid_select = 200
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]
	
	# Crea una matriz en la que se guardan los indices, R0 y suma juegos
	datos = pd.to_numeric(items[columna].tolist())

	ind = range(0, len(r0))
	l = np.concatenate((ind, r0, datos))
	l = l.reshape(3, len(r0))
	l = l.T
	
	# Ordena la matriz
	if jugado == 0:
		l = l[np.where(l[:,1] == 0)]  # deja en la matriz los juegos no jugados
	elif jugado == 1:
		l = l[np.where(l[:,1] == 1)]  # deja en la matriz los juegos si jugados
		
	l = l[l[:,2].argsort()]
	l = np.flipud(l)
	
	seleccion = ejecuta_seleccion (id_user, l, items, y, r, unid_select)
		
	return seleccion

	
def select_busqueda(id_user, palabra_busq):
	unid_select = 100
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]
	
	# Crea lista con distancia (Levenshtein )
	distancia = list()
	for i in range(len(r0)):
		palabra = items.loc[i][0]
		dist_min = np.inf
		for p in palabra.split():
			dist = jel.levenshtein_distance(palabra_busq, p)
			if dist < dist_min:
				dist_min = dist
		distancia.append(dist_min)

	# Crea una matriz en la que se guardan los indices, R0 y distancia
	ind = range(0, len(r0))
	l = np.concatenate((ind, r0, distancia))
	l = l.reshape(3, len(r0))
	l = l.T
	
	# Ordena la matriz
	l = l[l[:,2].argsort()]
	#l = np.flipud(l)
	
	seleccion = ejecuta_seleccion (id_user, l, items, y, r, unid_select)
		
	return seleccion

	
def ejecuta_seleccion (id_user, l, items, y, r, unid_select):
	seleccion = list()
	linea_select_a = list()
	linea_select_b = list()

	if unid_select > len(l):
		unid_select = len(l)
		
	for i in range (unid_select):
		juego = int(l[i][0])
		linea_select_a = items.loc[juego].values.tolist()
		linea_select_b = calcula_estad_juego(juego,y,r)
		valor = int(y[juego,id_user])
		
		seleccion.append(linea_select_a + linea_select_b + [valor, juego, id_user])
		
	return seleccion
	

def actualizaSelec(id_juego, valor, seleccion_total):
	# Recorre todas las selecciones que incluya el total
	for slc_parcial in seleccion_total:
	
		# Recorre la seleccion en particular
		for slc in slc_parcial['select']:
		
			# Actualiza los valores del juego si existe
			if slc[15] == id_juego:
				
				# slc[8] == Numero usuarios     #slc[14] == Puntuacion
				# slc[9] - slc[13] == 5 stars - 1 star
				# Si la puntuacion anterior era 0 -> ahora hay un user más
				if slc[14] == 0:
					slc[8] = slc[8] + 1
					
				# Actualiza según valores recibidos
				
				if valor == 0:
					slc[8] = slc[8] - 1
					if slc[14] == 1:
						slc[13] = slc[13] - 1
					elif slc[14] == 2:
						slc[12] = slc[12] - 1
					elif slc[14] == 3:
						slc[11] = slc[11] - 1
					elif slc[14] == 4:
						slc[10] = slc[10] - 1
					elif slc[14] == 5:
						slc[9] = slc[9] - 1

				elif valor == 1:
					slc[13] = slc[13] + 1
					if slc[14] == 2:
						slc[12] = slc[12] - 1
					elif slc[14] == 3:
						slc[11] = slc[11] - 1
					elif slc[14] == 4:
						slc[10] = slc[10] - 1
					elif slc[14] == 5:
						slc[9] = slc[9] - 1
					
				elif valor == 2:
					slc[12] = slc[12] + 1
					if slc[14] == 1:
						slc[13] = slc[13] - 1
					elif slc[14] == 3:
						slc[11] = slc[11] - 1
					elif slc[14] == 4:
						slc[10] = slc[10] - 1
					elif slc[14] == 5:
						slc[9] = slc[9] - 1
						
				elif valor == 3:
					slc[11] = slc[11] + 1
					if slc[14] == 1:
						slc[13] = slc[13] - 1
					elif slc[14] == 2:
						slc[12] = slc[12] - 1
					elif slc[14] == 4:
						slc[10] = slc[10] - 1
					elif slc[14] == 5:
						slc[9] = slc[9] - 1			
						
				elif valor == 4:
					slc[10] = slc[10] + 1
					if slc[14] == 1:
						slc[13] = slc[13] - 1
					elif slc[14] == 2:
						slc[12] = slc[12] - 1
					elif slc[14] == 3:
						slc[11] = slc[11] - 1
					elif slc[14] == 5:
						slc[9] = slc[9] - 1						

				elif valor == 5:
					slc[9] = slc[9] + 1
					if slc[14] == 1:
						slc[13] = slc[13] - 1
					elif slc[14] == 2:
						slc[12] = slc[12] - 1
					elif slc[14] == 3:
						slc[11] = slc[11] - 1
					elif slc[14] == 4:
						slc[10] = slc[10] - 1					
				
				# Puntuacion y  Media
				slc[14] = valor
				slc[6] = str("{:.1f}".format((slc[9]*5 + slc[10]*4 + slc[11]*3 + slc[12]*2 + slc[13])/slc[8]))
				slc[7] = imagen_puntuacion((slc[9]*5 + slc[10]*4 + slc[11]*3 + slc[12]*2 + slc[13])/slc[8])
				
			# fin si es cambio
		
		# fin for parcial
	#fin for total
	return seleccion_total
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	