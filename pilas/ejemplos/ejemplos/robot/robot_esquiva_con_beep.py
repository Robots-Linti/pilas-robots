# -*- encoding: utf-8 -*-

import pilas
from pilas.actores import Actor
from pilas.actores import Fantasma
from pilas.actores import Aceituna


def incrementarEscala(actores, escala):
    for f in  actores:
        f.escala = escala
    

class Personaje():
	def __init__(self, robot):
		self.robot = robot
		self.obstaculos = 0
	def esquiva(self):
		self.robot.backward(40, 1)
		self.robot.turnRight(50, 0.5)
		self.robot.forward()
 
pilas.iniciar()

fan = pilas.actores.Fantasma() * 8
aceitunas = pilas.actores.Aceituna() * 8

incrementarEscala(fan, 3)
incrementarEscala(aceitunas, 2)

b = pilas.actores.Board("/dev/tty/USB0")
robot = pilas.actores.Robot(b, 1)
robot.subelapiz()

robot.x = - 30
robot.y = -50
global obstaculos
obstaculos = 0
p = Personaje(robot)
# Esquiva 10 obstáculos

def hayObstaculo(personaje,obstaculos):
	if personaje.robot.getObstacle(15):
		personaje.obstaculos = personaje.obstaculos + 1
		personaje.robot.beep(200,1)
		personaje.esquiva()
	if personaje.obstaculos == 4:
		personaje.robot.stop()
		return False
	print personaje.obstaculos
	personaje.robot.forward()
	return True	
	
robot.backward(40, 1)
robot.turnRight(50, 0.5)
pilas.mundo.agregar_tarea(1, hayObstaculo, p, obstaculos)
robot.stop()


pilas.ejecutar()
