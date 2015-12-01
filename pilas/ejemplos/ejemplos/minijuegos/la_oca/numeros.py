import pilas
from pilas.actores import Actor


class Numero (Actor):

    def __init__(self, x=0, y=0, n=0):
        self.num = n

        self.pic0 = pilas.imagenes.cargar("data/imagenes/numeros/0.png")
        self.pic1 = pilas.imagenes.cargar("data/imagenes/numeros/1.png")
        self.pic2 = pilas.imagenes.cargar("data/imagenes/numeros/2.png")
        self.pic3 = pilas.imagenes.cargar("data/imagenes/numeros/3.png")
        self.pic4 = pilas.imagenes.cargar("data/imagenes/numeros/4.png")
        self.pic5 = pilas.imagenes.cargar("data/imagenes/numeros/5.png")
        self.pic6 = pilas.imagenes.cargar("data/imagenes/numeros/6.png")
        self.pic7 = pilas.imagenes.cargar("data/imagenes/numeros/7.png")
        self.pic8 = pilas.imagenes.cargar("data/imagenes/numeros/8.png")
        self.pic9 = pilas.imagenes.cargar("data/imagenes/numeros/9.png")
        self.pic10 =  pilas.imagenes.cargar("data/imagenes/numeros/10.png")

        Actor.__init__(self, x=x, y=y)
        
        if self.num == 1:
            self.imagen = self.pic1
        elif self.num== 2:
            self.imagen = self.pic2
        elif self.num==3:
            self.imagen = self.pic3
        elif self.num==4:
            self.imagen = self.pic4
        elif self.num==5:
            self.imagen = self.pic5
        elif self.num==6:
            self.imagen = self.pic6
        elif self.num==7:
            self.imagen = self.pic7
        elif self.num==8:
            self.imagen = self.pic8
        elif self.num==9:
            self.imagen = self.pic9
        elif self.num==10:
            self.imagen = self.pic10
        else :
            self.imagen = self.pic0

    def cambiar_numero(self, n=0):
        self.num = n
        # falta animacion
        self.cambiar_pic()

    def get_numero (self):
        return self.num

    def cambiar_pic(self):
        if self.num == 1:
            self.imagen = self.pic1
        elif self.num== 2:
            self.imagen = self.pic2
        elif self.num==3:
            self.imagen = self.pic3
        elif self.num==4:
            self.imagen = self.pic4
        elif self.num==5:
            self.imagen = self.pic5
        elif self.num==6:
            self.imagen = self.pic6
        elif self.num==7:
            self.imagen = self.pic7
        elif self.num==8:
            self.imagen = self.pic8
        elif self.num==9:
            self.imagen = self.pic9
        elif self.num==10:
            self.imagen = self.pic10
        else :
            self.imagen = self.pic0



