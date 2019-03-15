# -*- coding: utf-8 -*-
"""
Utilización selenium con chromedriver
sobre la web http://www.python.org
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
if not "Python" in driver.title:
	raise AssertionError()

print (driver.title)

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

if "No results found." in driver.page_source:
	raise AssertionError()

driver.close()