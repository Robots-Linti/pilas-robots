import pilas
from pilas.actores import Actor


class Animal(Actor):

    def __init__(self, animal, x=0, y=0):
        self.animal = animal.lower()
        Actor.__init__(self, x=x, y=y)
        ruta="data/imagenes/animales/"+str(self.animal)+'.png'
        self.imagen = pilas.imagenes.cargar(ruta)


    def get_animal (self):
        return self.animal

    def cambiar_pic(self):
        ruta="data/imagenes/animales/"+str(self.animal)+'.png'
        self.pic = pilas.imagenes.cargar(ruta)


