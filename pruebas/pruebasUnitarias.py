# -*- coding: utf-8 -*-
"""
Pruebas unitarias
"""

import unittest
import numpy as np
import csv


class PruebasUnitarias(unittest.TestCase):
    
            
	def test_datos_juegos(self):
		with open(r'..\src\app\static\datos\datosJuegos.csv', 'r') as csvfile:
			file = csv.reader(csvfile, delimiter ='\n')
			for linea_juego in file:
				self.assertEqual (linea_juego[0].count(";"),5)

            
            
	def test_y (self):
		y = np.load(r'..\src\app\static\datos\Y.npy')
		n_juegos, n_users = y.shape
		self.assertEqual(n_users, 1000)


	def test_r (self):
		r = np.load(r'..\src\app\static\datos\R.npy')
		y = np.load(r'..\src\app\static\datos\y.npy')
		n_juegos, n_users = r.shape
		self.assertEqual(n_users, 1000)
		r2 = np.zeros ((n_juegos, n_users), dtype = np.int)
		r2[y>0]=1
		self.assertEqual(r.all(), r2.all())

            
        
	def test_p_modelos (self):
		p_modelos = np.load(r'..\src\app\static\datos\P_Modelos.npy')
		p2 = np.where(p_modelos < 0)
		self.assertEqual (len(p2[0]),0)
		p2 = np.where(p_modelos > 5)
		self.assertEqual (len(p2[0]),0)



	def test_p_mem_users (self):
		p_mem_users = np.load(r'..\src\app\static\datos\P_Mem_Users.npy')
		p2 = np.where(p_mem_users < 0)
		self.assertEqual (len(p2[0]),0)
		p2 = np.where(p_mem_users > 5)
		self.assertEqual (len(p2[0]),0)



	def test_p_mem_juegos (self):
		p_mem_juegos = np.load(r'..\src\app\static\datos\P_Mem_Juegos.npy')
		p2 = np.where(p_mem_juegos < 0)
		self.assertEqual (len(p2[0]),0)
		p2 = np.where(p_mem_juegos > 5)
		self.assertEqual (len(p2[0]),0)



if __name__ == '__main__':
	unittest.main()
