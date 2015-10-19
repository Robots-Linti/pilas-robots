# -*- encoding: utf-8 -*-
import pilas



		
pilas.iniciar()
class Cont():
	def __init__(self):
		self.cont = 0
c = Cont()
b = pilas.actores.Board("/dev/tty/USB0")
r = pilas.actores.Robot(b,1)
r.subelapiz()

r.bajalapiz()

pilas.avisar("El robot hace zigzag")

def hacer(r,c):
	if c.cont == 0:
		r.forward(50)
	if c.cont == 1:
		r.turnLeft(40)
	if c.cont == 2:
		r.forward(100)
	if c.cont == 3:
		r.turnRight(80)
	if c.cont == 4:
		r.forward(100)
	if c.cont == 5:
		r.stop()
		return False
	c.cont = c.cont + 1
	return True
		

pilas.mundo.agregar_tarea(2, hacer, r, c)
pilas.ejecutar()
