coverage erase
rd htmlcov /S
coverage run --branch pruebasUnitarias.py
coverage xml -i
coverage html