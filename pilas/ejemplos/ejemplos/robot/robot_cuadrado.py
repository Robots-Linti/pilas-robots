# -*- encoding: utf-8 -*-
import pilas



pilas.iniciar()

b = pilas.actores.Board("/dev/tty/USB0")
r = pilas.actores.Robot(b, 1)
class RoCuadrado():
	def __init__(self):
		self.cant = 0
		
pilas.avisar("El Robor hace un cuadrado.")
ro = RoCuadrado()


    
def hacer(ro, r):
	if ro.cant%2 == 0:
		r.forward(100)
	if ro.cant%2 != 0 :
		r.turnLeft(100)
	if ro.cant == 8:
		r.stop()
		return False
	ro.cant = ro.cant + 1
	
	return True

    


pilas.mundo.agregar_tarea(1.6, hacer, ro, r )


pilas.ejecutar()
