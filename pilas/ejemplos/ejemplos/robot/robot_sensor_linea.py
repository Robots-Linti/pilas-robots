# -*- encoding: utf-8 -*-

# Importat la librería 
import pilas
from pilas.utils import obtener_ruta_al_recurso
pilas.iniciar()


# Definición de actores
b = pilas.actores.Board("/dev/tty/USB0")
r = pilas.actores.Robot(b, 1)

# Cargar el fondo a evaluar


pilas.fondos.FondoPersonalizado(obtener_ruta_al_recurso('robot_sensor_lineas.png'))    

# Avance del robot
r.forward(50)


def linea (r):
	iq, dr = r.getLine()
	if iq != 255.0 and  dr != 255.0:
		print iq, dr
		return True
	else:
		r.stop()
		return False


pilas.mundo.agregar_tarea(0.5, linea, r)

#~ r.stop()
pilas.ejecutar()
