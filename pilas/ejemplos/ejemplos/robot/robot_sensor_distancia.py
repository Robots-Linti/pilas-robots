# -*- encoding: utf-8 -*-

# Importat la librería 
import pilas

#Inniciar 
pilas.iniciar()


# Definición de los actores
b = pilas.actores.Board("/dev/tty/USB0")
r = pilas.actores.Robot(b, 1)
m = pilas.actores.Mono()


# Posiciones de los actores
r.x = 11
r.y = -30
m.x = 15
m.y = 140


def distancia(r,m):
	if (r.ping() > 10):
		pilas.avisar("Distancia entre el Robot y el Mono: " +  str(r.ping()))
	else:
		m.decir("Cuidado!!!!!")
		r.stop()
		return False
	r.forward()
	return True



pilas.mundo.agregar_tarea(1, distancia, r,m)


pilas.ejecutar()
