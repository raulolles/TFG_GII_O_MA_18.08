# -*- coding: utf-8 -*-
"""
Utilización de Selenium y Chromedriver
para realizar pruebas unittest
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        if "No results found." not in driver.page_source:
            raise AssertionError()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
