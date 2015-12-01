import os
import sys
directorio_actual = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(directorio_actual, 'la_oca'))
sys.path.insert(0, os.path.join(directorio_actual, 'la_oca'))
import ejecutar
