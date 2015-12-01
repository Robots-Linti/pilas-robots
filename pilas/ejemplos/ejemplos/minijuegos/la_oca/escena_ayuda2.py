# -*- coding: cp1252 -*-
import pilas

from pilas.escena import Base

TEXTO = '''El objetivo es  formar la palabra correspondiente
a un animal. Se tienen una cantidad de puntos iniciales,
los cuales se restan 50 si deseas ver la foto del animal
("ver foto") y 10 si quieres ver la definicion de este
("ver definicion") Cuando termines de colocar las letras
que creas correspondientes a casa casillero, has click en "Listo",
si esta bien se dara como finalizado en juego y sumaras tantos
puntos como hayas logrado. De lo contrario se te quitara una vida.
Si pierdes las tres vidas, perderas una en el juego principal.'''

def crear_texto_ayuda():
    ayuda = pilas.actores.Texto("Ayuda\n \n \nADIVINA EL ANIMAL",x=-700,y=500, fuente="data/tipografias/Insanibu.ttf")
    ayuda.escala = 1.3
    ayuda.x= [-300]
    ayuda.y= [250]
    texto = pilas.actores.Texto(TEXTO, y=-400)
    texto.y=[0]
    texto.color = pilas.colores.amarillo
    pilas.avisar("Pulsa ESC para ir al juego",25)

def volver(self, *k, **kv):
    pilas.recuperar_escena()


class ayuda_minijuego(Base):

    def __init__(self):
        Base.__init__(self)


    def iniciar(self):
        pilas.fondos.Color(pilas.colores.marron)
        crear_texto_ayuda()
        self.pulsa_tecla_escape.conectar(volver)



#Para chequear funcionamiento
'''pilas.iniciar(1024,712)
         	
pilas.mundo.motor.alto_original = 712
pilas.mundo.motor.ancho_original = 1024
pilas.cambiar_escena(ayuda_juego())
pilas.ejecutar()'''

