coverage erase
rd htmlcov /S
coverage run --source=..\src\app\filtros,..\src\app\genera_datos --branch pruebasUnitarias.py
coverage xml -i
coverage html