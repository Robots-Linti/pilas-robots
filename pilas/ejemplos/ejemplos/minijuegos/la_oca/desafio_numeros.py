# -*- coding: cp1252 -*-
import pilas
import random
import pickle

from pilas.escena import Base
from numeros import Numero

class minijuego_numeros(Base):

    def __init__(self):
        Base.__init__(self)
        self.palabras=['CERO','UNO','DOS','TRES','CUATRO','CINCO','SEIS','SIETE','OCHO','NUEVE','DIEZ']
        self.sonido_ok = pilas.sonidos.cargar("data/musica/youpee.ogg")
        self.sonido_great = pilas.sonidos.cargar("data/musica/yay_sound.ogg")
        self.sonido_bad = pilas.sonidos.cargar("data/musica/aww_sound.ogg")

    def iniciar(self):
        pilas.fondos.Color(pilas.colores.negro)
        #Iniciamoz titulo y consigna de juego
        titulo = pilas.actores.Texto("Conecta numeros y palabras", fuente="tipografias/Alpha Romanie Outline G98.ttf", y=400)
        titulo.escala = 3
        titulo.color = pilas.colores.naranja
        titulo.y = [200],2
        self.primera_vista()


    def primera_vista(self):
        bOk= pilas.interfaz.Boton("ENTENDIDO",y=-190)
        consigna = pilas.actores.Texto('Coloca la palabra en el cuadro punteado \n debajo del numero que corresponda.\n\n presiona "Continuar" cuando termines.',
                                       fuente="tipografias/Insanibu.ttf")
        nota = pilas.actores.Texto("Sumaras 10 puntos por respuesta correcta. \n En caso de que respondas las tres mal, \n se te descontara una vida.",
                                   fuente="tipografias/Insanibu.ttf",y=-100)
        def entendido():
            bOk.eliminar()
            consigna.eliminar()
            nota.eliminar()
            self.crear_escenario()
        bOk.conectar(entendido)

    def crear_escenario(self):
        #Cramos puntaje
        self.puntos = pilas.actores.Puntaje(x=400, y=300, color=pilas.colores.rojo)
        pilas.fondos.Color(pilas.colores.amarillo)
        #Creamos actor interactuante
        self.actor = pilas.actores.Actor(x=700, y=-330)
        self.actor.x = [450],0.5
        self.actor.imagen = pilas.imagenes.cargar("data/imagenes/varios/actor.png")
        #Se eligen tres numeros
        numeros_elegidos =[]
        for i in range(3):
            n = random.randrange(0,11)
            while n in numeros_elegidos: n = random.randrange(0,11)
            numeros_elegidos.append(n)

        #Se crean carteles
        self.carteles = pilas.grupo.Grupo()
        self.numeros = pilas.grupo.Grupo()
        self.punteados = pilas.grupo.Grupo()
        posxc = [-300,0,300]
        posxn = [-370,0,370]

        for i in numeros_elegidos:
            #Creamos Numero
            xn = random.choice(posxn)
            posxn.remove(xn)
            n = Numero(n=i, x=xn)
            self.numeros.append(n)
            #Cuadro punteado
            cp = pilas.actores.Actor(pilas.imagenes.cargar("data/imagenes/varios/cuadro punteado.png"), x=xn, y=-120)
            cp.radio_de_colision=30
            #cp.radio_de_colision.forma = rectangulo
            self.punteados.append(cp)
            #Creamos cartel
            xc = random.choice(posxc)
            posxc.remove(xc)
            pal = self.palabras[i]
            c = pilas.actores.Texto(pal, fuente="data/tipografias/American Captain.ttf", x=xc, y=-300)
            c.color = pilas.colores.azuloscuro
            c.escala = 2.5
            c.aprender(pilas.habilidades.Arrastrable)
            self.carteles.append(c)

        self.boton_continuar = pilas.interfaz.Boton("CONTINUAR", y=-230)
        self.boton_continuar.conectar(self.continuar)
        def ubicar(cartel,punteado):
            cartel.x = punteado.x
            cartel.y = punteado.y
        self.colisiones.agregar(self.carteles,self.punteados,ubicar)

    def terminar(self):
        self.boton_continuar.eliminar()
        self.actor.y=[200],1.5
        for i in self.carteles:
            i.eliminar_habilidad(pilas.habilidades.Arrastrable)
        bien = pilas.imagenes.cargar("data/imagenes/varios/OK.png")
        mal = pilas.imagenes.cargar("data/imagenes/varios/NOT.png")
        for i in range(3):
            pos = self.numeros[i].x + 80
            if self.punteados[i].colisiona_con(self.carteles[i]):
                marca = pilas.actores.Actor(bien,x=pos)
                self.puntos.aumentar(10)
            else:
                marca = pilas.actores.Actor(mal,x=pos)
                self.carteles[i].color = pilas.colores.rojo
                self.carteles[i].x  = [self.punteados[i].x]
                self.carteles[i].y  = [self.punteados[i].y]
        self.punteados.eliminar()
        boton_salir = pilas.interfaz.Boton("Seguir jugando",x=350,y=-340)
        def volver_a_jugar():
            boton_salir.desactivar()
            pilas.recuperar_escena()
        boton_salir.conectar(volver_a_jugar)
        self.sumar_puntaje()

    def sumar_puntaje(self):
        puntos = self.puntos.obtener()
        if puntos == 0 :
            puntos = -1
            self.actor.decir("Lo siento, perdiste una vida!",3)
            self.sonido_bad.reproducir()
        else:
            self.actor.decir("Felicitaciones, sumaste %s puntos!"% puntos)
            if puntos==30:
                self.sonido_great.reproducir()
            else:
                self.sonido_ok.reproducir()
        archivo = open("data/ultimo_puntaje.txt",'wb')
        pickle.dump(puntos,archivo)
        archivo.close()

    def continuar(self):
        self.boton_continuar.desactivar()
        #Podria haber opcion de confirmaci?n
        self.terminar()

'''pilas.iniciar(1024,712)

pilas.mundo.motor.alto_original = 712
pilas.mundo.motor.ancho_original = 1024
musica = pilas.sonidos.cargar("data/musica/Sneaky_Adventure.ogg")
pilas.cambiar_escena(minijuego_numeros())

pilas.ejecutar()'''
