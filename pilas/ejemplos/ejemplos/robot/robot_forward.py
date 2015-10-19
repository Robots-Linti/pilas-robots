import pilas
pilas.iniciar()
b = pilas.actores.Board("/dev/tty/USB0")
r = pilas.actores.Robot(b,1)
	
def hacer(r):
	r.stop()
	return False
		
r.forward()
pilas.mundo.agregar_tarea(4, hacer, r )


pilas.ejecutar()
