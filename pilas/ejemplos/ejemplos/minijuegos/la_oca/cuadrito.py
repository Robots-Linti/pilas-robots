import pilas
from pilas.actores import Actor

class cuadro_para_letra(Actor):

    def __init__(self,x=0,y=0):
        imagen = pilas.imagenes.cargar("data/imagenes/varios/cuadrito.png")
        Actor.__init__(self,x=x,y=y)
        self.imagen = imagen

    def set_letra (self, letra=''):
        self.letra = str(letra)
        self.letra_puesta = ''

    def set_colision(self, letra=''):
        self.letra_puesta = str(letra)

    def get_colision(self):
        try:
            return self.letra_puesta
        except:
            return ''

    def get_letra(self):
        return self.letra

    def correcto(self):
        l1 = self.letra
        l2 = self.letra_puesta
        return l1==l2

