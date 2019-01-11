import numpy as np
from pandas import read_table
import random


def select_de_matriz(p,r,id_user,unid_select,items):
	# Crea una matriz en la que se guardan los indices, R0 y P0
	p0= p[:,id_user]
	ind = range(0, len(r))
	l = np.concatenate((ind, r, p0))
	l = l.reshape(3, len(r))
	l = l.T

	# Selecciona valores y Ordena la matriz
	l = l[np.where(l[:,1] == 0)]  # deja en la matriz los juegos no jugados
	l = l[l[:,2].argsort()]       # ordena la matriz por P
	l = np.flipud(l)              # voltea la matriz para ofrecer en orden correcto

	seleccion = items.loc[l[:,0][0:unid_select]].values.tolist()
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
	
	
def select(id_user):
	unid_select = 5
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	r0 = r[:,id_user]

	select_users = select_de_matriz(p_mem_users,r0,id_user,unid_select,items)	
	select_juegos = select_de_matriz(p_mem_juegos,r0,id_user,unid_select,items)
	select_modelos = select_de_matriz(p_modelos,r0,id_user,unid_select,items)

	return select_modelos, select_users, select_juegos
	
def select_aleatorio():
	unid_select = 5
	y, r, p_modelos, p_mem_users, p_mem_juegos, items = importa_tablas()
	n_juegos,n_users = y.shape
	n_juegos = n_juegos-1
	select = list()
	
	for i in range (unid_select):
		select.append(items.loc[random.randint(0,n_juegos)].values.tolist())
	
	return select