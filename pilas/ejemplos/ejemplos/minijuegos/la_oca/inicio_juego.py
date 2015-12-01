import pilas
import time
from pilas.escena import Base
from sonido import Sonido
from escena_juego import Juego

def volver_al_menu(*k, **kv):
        pilas.recuperar_escena()

class ingreso_datos(Base):

    def __init__(self):
        Base.__init__(self)
        self.nombre = ''

    def variable_datos(self, nombre=''):
        self.nombre = str(nombre)
        dia=time.strftime("%d/%m/%y")
        datos = nombre + ' - ' + dia
        return str(datos)

    def rotacion_actor(self,n=0):
        self.actor.rotacion = n

    def cambiar_escena(self):
        # reemplazar por cambio de escena enviar var self.info_juego
        name = str(self.info_juego)
        pilas.cambiar_escena(Juego(name))

    def comenzar_a_jugar(self):
        #pilas.avisar("%s"%self.info_juego)
        self.actor.x = [0]
        self.actor.y = [-30]
        def ver_rta(r):
            self.actor.x = [-700],1
            self.actor.y = [200],1
            pilas.mundo.agregar_tarea(1.3,self.cambiar_escena)
        self.d.elegir(self.actor,"Estas listo %s?" % self.nombre,['>> Si! a jugar...<<'],ver_rta)
        pilas.mundo.agregar_tarea(1.5,self.d.iniciar)


    def verificar(self):
        nombre = str(self.box.texto)
        self.box.desactivar()
        self.blisto.desactivar()
        if (len(nombre)<4):
            self.d.decir(self.actor,"Ingresa un nombre mas largo. Al menos 4 letras")
            self.box.activar()
            self.blisto.activar()
            self.d.iniciar()
        elif nombre.isdigit():
            self.d.decir(self.actor,"No solo numeros! intentalo de nuevo")
            self.box.activar()
            self.blisto.activar()
            self.d.iniciar()
        else :
            self.box.eliminar()
            self.blisto.eliminar()
            self.info_juego=self.variable_datos(nombre)
            self.comenzar_a_jugar()


    def continuar_animacion(self):
        self.box.mostrar()
        self.blisto = pilas.interfaz.Boton("Listo",x=205)
        self.blisto.conectar(self.verificar)
        self.d = pilas.actores.Dialogo()
        self.d.decir(self.actor,"Hola! Ingresa tu nombre \n para comenzar a jugar.")
        self.d.iniciar()


    def iniciar(self):
        pilas.fondos.Fondo("data/imagenes/fondos/fondo_neutro.jpg")
        pilas.avisar("Preciona ESC para volver al menu")
        self.pulsa_tecla_escape.conectar(volver_al_menu)
        #Iniciamos actor interactor
        self.actor = pilas.actores.Actor("data/imagenes/varios/actor.png",x=600)
        self.actor.rotacion = 330
        #Ingreso de texto
        self.box = pilas.interfaz.IngresoDeTexto(ancho=200)
        self.box.ocultar()
        self.box.escala = 1.5
        #animacion
        self.actor.x = [220]
        self.actor.y = [140],2
        pilas.mundo.agregar_tarea(2,self.rotacion_actor)
        pilas.mundo.agregar_tarea(2.3,self.continuar_animacion)


'''pilas.iniciar(1024,712,titulo="La oca")
         	
pilas.mundo.motor.alto_original = 712
pilas.mundo.motor.ancho_original = 1024
m = pilas.sonidos.cargar("data/musica/Sneaky_Adventure.ogg")
pilas.cambiar_escena(ingreso_datos())

pilas.ejecutar()'''
