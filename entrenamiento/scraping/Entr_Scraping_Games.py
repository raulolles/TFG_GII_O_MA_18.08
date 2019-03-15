# -*- coding: utf-8 -*-
"""
Prueba de entrenamiento realizada sobre la web
https://archive.org/details/softwarelibrary_c64_games

Se realizan diferentes pruebas de scraping para:
    - Probar la estructura de la web
    - Practicar  scraping
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://archive.org/details/softwarelibrary_c64_games")

print('---------------------------------------------------')
print('Primera prueba Scraping (Python Selenium) sobre web\n')

assert "C64" in driver.title
print("  --> Driver Title: \n", driver.title, "\n")

titulo = driver.find_element_by_tag_name('title')
print("  --> Etiqueta 'title': \n", titulo.text, "\n")

h1 = driver.find_element_by_tag_name('h1')
print("  --> Etiqueta 'h1'        : ", h1.text)
print("  --> Tag_name 'h1'        : ", h1.tag_name)
print("  --> Loaclización 'h1'    : ", h1.location)
print("  --> Tamaño 'h1'          : ", h1.size, "\n")


elem = driver.find_elements_by_xpath("//div [@class='item-ia hov']")


for e in elem:
    juego = e.text.split('\n')
    long= len(juego)
    juego[1] = juego[1][3:]
    print(juego)
            

print('\n  --> Total Juegos: ', len(elem))


driver.close()