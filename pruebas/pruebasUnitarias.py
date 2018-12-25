# -*- coding: utf-8 -*-
"""
Pruebas unitarias
"""

import unittest
import numpy as np
import csv


class PruebasUnitarias(unittest.TestCase):
    
            
    def test_datosJuegos(self):
        try:
            with open('..\src\datos\datosJuegos.csv', 'r') as csvfile:
                file = csv.reader(csvfile, delimiter ='\n')
                for lineaJuego in file:
                    self.assertEqual (lineaJuego[0].count(";"),5)
        except IOError as e:
            print("\n --> Error en test_datosJuegos:  Verifique que existe el fichero datosJuego")
            print ("       I/O error({0}): {1}".format(e.errno, e.strerror))
            
            
    def test_Y (self):
        try:
            Y = np.load('..\src\datos\Y.npy')
            nJuegos, nUsers = Y.shape
            self.assertEqual(nUsers, 1000)
        except IOError as e:
            print ("\n --> Error en test_Y:  Verifique que existe la matriz Y")
            print ("       I/O error({0}): {1}".format(e.errno, e.strerror))
        

    def test_R (self):
        try:
            R = np.load('..\src\datos\R.npy')
            Y = np.load('..\src\datos\Y.npy')
            nJuegos, nUsers = R.shape
            self.assertEqual(nUsers, 1000)
            R2 = np.zeros ((nJuegos, nUsers), dtype = np.int)
            R2[Y>0]=1
            self.assertEqual(R.all(), R2.all())
        except IOError as e:
            print ("\n --> Error en test_R:  Verifique que existe la matriz R e Y")
            print ("       I/O error({0}): {1}".format(e.errno, e.strerror))
            
        
if __name__ == '__main__':
    unittest.main()
