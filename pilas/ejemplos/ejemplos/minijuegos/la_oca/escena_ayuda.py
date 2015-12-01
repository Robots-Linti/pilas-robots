# -*- coding: cp1252 -*-
import pilas

from pilas.escena import Base

TEXTO = '''El objetivo es llegar a la meta con la mayor cantidad de puntos
posible. Para moverte en el tablero debes ir tirando el dado (haciendo click en el).
Cada casillero tiene un elemento diferente con distintos significados. Los desafios,
como las preguntas, son para sumar puntos, con la diferencia que
si los pierdes, perderas una vida.'''

def crear_texto_ayuda():
    ayuda = pilas.actores.Texto("Ayuda",x=-700,y=500, fuente="data/tipografias/Insanibu.ttf")
    ayuda.escala = 1.3
    ayuda.x= [-400]
    ayuda.y= [330]
    texto = pilas.actores.Texto(TEXTO, y=-400)
    texto.y=[240]
    texto.color = pilas.colores.amarillo
    pilas.avisar("Pulsa ESC para regresar",40)

def volver(self, *k, **kv):
    pilas.recuperar_escena()


class ayuda_juego(Base):

    def __init__(self):
        Base.__init__(self)


    def iniciar(self):
        pilas.fondos.Fondo("data/imagenes/fondos/ayuda.jpg")
        crear_texto_ayuda()
        self.pulsa_tecla_escape.conectar(volver)



#Para chequear funcionamiento
'''pilas.iniciar(1024,712)
         	
pilas.mundo.motor.alto_original = 712
pilas.mundo.motor.ancho_original = 1024
pilas.cambiar_escena(ayuda_juego())
pilas.ejecutar()'''

