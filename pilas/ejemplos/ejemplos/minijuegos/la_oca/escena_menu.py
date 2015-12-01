import pilas
import random
import pickle

from pilas.escena import Base
from escena_ayuda import ayuda_juego
from escena_puntajes import Puntajes
from inicio_juego import ingreso_datos
from sonido import Sonido

def ver_ayuda():
    pilas.almacenar_escena(ayuda_juego())

def ver_puntaje():
    pilas.almacenar_escena(Puntajes())

def salir():
    import sys
    sys.exit(0)


class Menu(Base):

    def __init__(self):
        Base.__init__(self)

    def iniciar(self):
        self.iniciar_sonido()
        self.iniciar_fondo()
        self.iniciar_menu()
        #Titulo
        self.titulo = pilas.actores.Actor("data/imagenes/varios/titulo.png",y=250)
        self.titulo.escala = [2,1],3

    def iniciar_sonido(self):
        try:
            f = open("data/estado_musica.txt",'rb')
            est = pickle.load(f)
            f.close()
        except :
            est = True
            f = open("data/estado_musica.txt",'wb')
            pickle.dump(est,f)
            f.close()
        self.m = pilas.sonidos.cargar("data/musica/Sneaky_Adventure.ogg")
        if est:  self.m.reproducir()
        self.musica = Sonido(musica=self.m, y=-250,estado=est)



    def iniciar_menu(self):
        cartel_menu = pilas.actores.Texto("M E N U",fuente="data/tipografias/American Captain.ttf",y=20)
        cartel_menu.escala=[4,2],3
        cartel_menu.color = pilas.colores.azuloscuro
        opciones = [('- Jugar -',self.comenzar_juego),('- Ayuda -',ver_ayuda),('- Ver puntajes -',ver_puntaje),(' - Salir -',salir)]
        self.menu = pilas.actores.Menu(opciones,y=-40,fuente="data/tipografias/American Captain.ttf")
        self.menu.escala = 1.4

    def comenzar_juego(self):
        self.m.detener()
        pilas.almacenar_escena(ingreso_datos())

    def iniciar_fondo(self):
        self.cont = 0
        pilas.fondos.Fondo("data/imagenes/fondos/menu.jpg")
        def crear_piedra(mensaje):
            #Elegimos parametros al azar
            tam = random.choice(["grande","media","chica"])
            px = random.randrange(-500,500)
            py = random.choice([-400,400])
            posibles_velocidades = range(-10, -2) + range(2, 10)
            cdx = 3
            cdy = 3
            p = pilas.actores.Piedra(tamano=tam, dx=cdx, dy=cdy, x=px, y=py)
            self.cont = self.cont + 1
            if self.cont < 10:
                return True
            else:
                return False
        pilas.mundo.agregar_tarea(3,crear_piedra, 1)







