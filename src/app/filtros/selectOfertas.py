import numpy as np
import pandas as pd
from pandas import read_table
import random
import jellyfish as jel

def calcula_estad_juego(juego,y,r):
	tabla_estad = list()
	
	y_juego = y[juego,:]
	users_jugado = int(np.sum(r[juego,:]))
	puntuacion = np.sum(y_juego)
	puntuacion_media = puntuacion/users_jugado
	imagen_punt = imagen_puntuacion(puntuacion_media)
	
	tabla_estad.append(str("{:.1f}".format(puntuacion_media)))
	tabla_estad.append(imagen_punt)
	tabla_estad.append(users_jugado)
	
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
	
	jugado = 0
	
	tabla_slc = crea_tabla_slc(p0, r0, True, jugado)	
	seleccion = ejecuta_seleccion (id_user, items, y, r, unid_select, tabla_slc)
		
	return seleccion
	
	
def select_predicciones(id_user):
	unid_select = 6
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()

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
	
	jugado = 1
	
	tabla_slc = crea_tabla_slc(y0, r0, True, jugado)	
	seleccion = ejecuta_seleccion (id_user, items, y, r, unid_select, tabla_slc)
		
	return seleccion

	
def select_mas_jugados(id_user, jugado):
	unid_select = 100
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]
	
	# Crea una matriz en la que se guardan los indices, R0 y suma juegos
	veces_jug = r.sum(axis = 1)

	tabla_slc = crea_tabla_slc(veces_jug, r0, True, jugado)	
	seleccion = ejecuta_seleccion (id_user, items, y, r, unid_select, tabla_slc)
	
	return seleccion

	
def select_mejor_valorados(id_user, jugado):
	unid_select = 100
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]
	
	# Crea una matriz en la que se guardan los indices, R0 y suma juegos
	valor_medio = y.sum(axis = 1) / r.sum(axis = 1)
	valor_medio[np.where(np.isnan(valor_medio))] = 0

	tabla_slc = crea_tabla_slc(valor_medio, r0, True, jugado)	
	seleccion = ejecuta_seleccion (id_user, items, y, r, unid_select, tabla_slc)
		
	return seleccion


def select_archive(id_user,columna,jugado):
	unid_select = 200
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]
	
	# Crea una matriz en la que se guardan los indices, R0 y suma juegos
	datos = pd.to_numeric(items[columna].tolist())

	tabla_slc = crea_tabla_slc(datos, r0, True, jugado)
	seleccion = ejecuta_seleccion (id_user, items, y, r, unid_select, tabla_slc)
		
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

	jugado = 3
	
	tabla_slc = crea_tabla_slc(distancia, r0, False, jugado)
	seleccion = ejecuta_seleccion (id_user, items, y, r, unid_select, tabla_slc)
		
	return seleccion

	
def crea_tabla_slc (criterio_slc, r0, ascendiente, jugado):
	# Crea una matriz en la que se guardan los indices, R0 y criterio_slc
	ind = range(0, len(r0))
	l = np.concatenate((ind, r0, criterio_slc))
	l = l.reshape(3, len(r0))
	l = l.T

	if jugado == 0:
		l = l[np.where(l[:,1] == 0)]  # deja en la matriz los juegos no jugados
	elif jugado == 1:
		l = l[np.where(l[:,1] == 1)]  # deja en la matriz los juegos si jugados
		
	# Ordena la matriz
	l = l[l[:,2].argsort()]
	
	if ascendiente:
		l = np.flipud(l)

	return l

def ejecuta_seleccion (id_user, items, y, r, unid_select, l):
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
	

def actualiza_selec(id_juego, valor, seleccion_total):
	# Recorre todas las selecciones que incluya el total
	for slc_parcial in seleccion_total:
	
		# Recorre la seleccion en particular
		for slc in slc_parcial['select']:
		
			slc = actualiza_selec2(slc, id_juego, valor)
		
		# fin for parcial
	#fin for total
	return seleccion_total
	
	
def actualiza_selec2(slc, id_juego, valor):
	# Actualiza los valores del juego si existe
	if slc[15] == id_juego:
		
		# slc[8] == Numero usuarios     #slc[14] == Puntuacion
		# slc[9] - slc[13] == 5 stars - 1 star
		
		if slc[14] == 0:
			slc[8] = slc[8] + 1
		else:
			ind_menos = 14 - slc[14]
			slc[ind_menos] = slc[ind_menos] - 1
					
		if valor == 0:
			slc[8] = slc[8] - 1
		else:
			ind_mas = 14 - valor
			slc[ind_mas] = slc[ind_mas] + 1
			
		# Puntuacion y  Media
		slc[14] = valor
		slc[6] = str("{:.1f}".format((slc[9]*5 + slc[10]*4 + slc[11]*3 + slc[12]*2 + slc[13])/slc[8]))
		slc[7] = imagen_puntuacion((slc[9]*5 + slc[10]*4 + slc[11]*3 + slc[12]*2 + slc[13])/slc[8])
	
	return slc
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	