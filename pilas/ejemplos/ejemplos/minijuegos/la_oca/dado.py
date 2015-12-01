import pilas

from pilas.actores import Boton
import random

class Dado(Boton):

    def __init__(self, x=0, y=0):

        #Se cargan imagenes
        self.cuadro_cero =  pilas.imagenes.cargar('data/imagenes/imagen_dado/0.png')
        self.cuadro_uno = pilas.imagenes.cargar('data/imagenes/imagen_dado/1.png')
        self.cuadro_dos = pilas.imagenes.cargar('data/imagenes/imagen_dado/2.png')
        self.cuadro_tres = pilas.imagenes.cargar('data/imagenes/imagen_dado/3.png')
        self.cuadro_cuatro = pilas.imagenes.cargar('data/imagenes/imagen_dado/4.png')
        self.cuadro_cinco = pilas.imagenes.cargar('data/imagenes/imagen_dado/5.png')
        self.cuadro_seis = pilas.imagenes.cargar('data/imagenes/imagen_dado/6.png')
        # inicializamos
        Boton.__init__(self, x=x, y=y)
        self.imagen = self.cuadro_cero
        self.num = 0
        self.sound = pilas.sonidos.cargar("data/musica/tick.wav")

    def definir_cuadro(self, indice=0):
        self.numero = indice
        if (indice == 1):
            self.imagen  = self.cuadro_uno
        elif (indice == 2):
            self.imagen = self.cuadro_dos
        elif (indice == 3):
            self.imagen = self.cuadro_tres
        elif (indice == 4):
            self.imagen = self.cuadro_cuatro
        elif (indice == 5):
            self.imagen = self.cuadro_cinco
        elif (indice == 6) :
            self.imagen = self.cuadro_seis
        else :
            self.imagen = self.cuadro_cero

    def numero (self):
        return self.num

    def tirar (self):
        #agregar animacion movimiento
        self.sound.reproducir()
        num = random.randrange(1,7)
        self.definir_cuadro(num)
        self.escala = [2,1]
        return num

