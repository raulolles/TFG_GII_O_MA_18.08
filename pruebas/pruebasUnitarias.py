# -*- coding: utf-8 -*-
"""
Pruebas unitarias
"""

import unittest
import numpy as np
import csv


class PruebasUnitarias(unittest.TestCase):
    
            
    def test_datos_juegos(self):
        try:
            with open(r'..\src\app\static\datos\datosJuegos.csv', 'r') as csvfile:
                file = csv.reader(csvfile, delimiter ='\n')
                for linea_juego in file:
                    self.assertEqual (linea_juego[0].count(";"),5)
        except IOError as e:
            print("\n --> Error en test_datos_juegos:  Verifique que existe el fichero datosJuego")
            print ("       I/O error({0}): {1}".format(e.errno, e.strerror))
            
            
    def test_y (self):
        try:
            y = np.load(r'..\src\app\static\datos\Y.npy')
            n_juegos, n_users = y.shape
            self.assertEqual(n_users, 1000)
        except IOError as e:
            print ("\n --> Error en test_Y:  Verifique que existe la matriz Y")
            print ("       I/O error({0}): {1}".format(e.errno, e.strerror))
        

    def test_r (self):
        try:
            r = np.load(r'..\src\app\static\datos\R.npy')
            y = np.load(r'..\src\app\static\datos\y.npy')
            n_juegos, n_users = r.shape
            self.assertEqual(n_users, 1000)
            r2 = np.zeros ((n_juegos, n_users), dtype = np.int)
            r2[y>0]=1
            self.assertEqual(r.all(), r2.all())
        except IOError as e:
            print ("\n --> Error en test_R:  Verifique que existe la matriz R e Y")
            print ("       I/O error({0}): {1}".format(e.errno, e.strerror))
            
        
    def test_p_modelos (self):
        try:
            p_modelos = np.load(r'..\src\app\static\datos\P_Modelos.npy')
            p2 = np.where(p_modelos < 0)
            self.assertEqual (len(p2[0]),0)
            p2 = np.where(p_modelos > 5)
            self.assertEqual (len(p2[0]),0)
        except IOError as e:
            print("\n --> Error en test_P_Modelos:  Verifique que existe la matriz P_Modelos")
            print ("       I/O error({0}): {1}".format(e.errno, e.strerror))


    def test_p_mem_users (self):
        try:
            p_mem_users = np.load(r'..\src\app\static\datos\P_Mem_Users.npy')
            p2 = np.where(p_mem_users < 0)
            self.assertEqual (len(p2[0]),0)
            p2 = np.where(p_mem_users > 5)
            self.assertEqual (len(p2[0]),0)
        except IOError as e:
            print("\n --> Error en test_P_Users:  Verifique que existe la matriz P_Mem_Users")
            print ("       I/O error({0}): {1}".format(e.errno, e.strerror))            


    def test_p_mem_juegos (self):
        try:
            p_mem_juegos = np.load(r'..\src\app\static\datos\P_Mem_Juegos.npy')
            p2 = np.where(p_mem_juegos < 0)
            self.assertEqual (len(p2[0]),0)
            p2 = np.where(p_mem_juegos > 5)
            self.assertEqual (len(p2[0]),0)
        except IOError as e:
            print("\n --> Error en test_P_Juegos:  Verifique que existe la matriz P_Mem_Juegos")
            print ("       I/O error({0}): {1}".format(e.errno, e.strerror)) 


if __name__ == '__main__':
    unittest.main()
