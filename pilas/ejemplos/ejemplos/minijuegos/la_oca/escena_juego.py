import pilas
import pickle
import random

from pilas.escena import Base
from sonido import Sonido
from vidas import ContadorDeVidas
from dado import Dado
from escena_ayuda import ayuda_juego
from desafio_numeros import minijuego_numeros
from desafio_animales import minijuego_animales


casillero_x = [-200,-200,-200,-200,-200,-200,-200,-122,-45,-45,-45,-45,-45,-45,-45,
                30,105,105,105,105,105,105,105,180,260,260,260,260,260,260,260,340,
                415,415,415,415,415,415,415,]
casillero_y = [-270,-190,-120,-45,35,110,190,190,190,115,35,-40,-115,-190,-270,
                -270,-270,-190,-115,-40,35,115,190,190,190,110,35,-40,-115,-190,
                -270,-270,-270,-190,-115,-40,35,110,190]
lista_desafios = [3,7,12,16,20,23,26,29,35]
lista_ret2 = [5,9,18,22,31,36]
lista_ret4 =[11,19,34]
lista_preg = [2,8,14,24,27,32]
lista_av2 = [6,30,15]
lista_av4 = [4,17,28]


def ver_ayuda():
    pilas.almacenar_escena(ayuda_juego())

def cerrar():
    import sys
    sys.exit(0)
    pilas.cambiar_escena(Menu())
    pass


class Juego(Base):

    def __init__(self,nombre=''):
        Base.__init__(self)
        self.musica = pilas.sonidos.cargar("data/musica/Two_Finger_Johnny.ogg")
        self.nombre = nombre
        self.puntos_fin = 0
        self.fin = False
        self.pos = 0
        self.nivel=1
        self.inf2=False
        self.inf3=False
        self.sonido_fallo = pilas.sonidos.cargar("data/musica/fail_sound.ogg")
        self.sonido_bien = pilas.sonidos.cargar("data/musica/ok_sound.ogg")
        self.sonido_llegada = pilas.sonidos.cargar("data/musica/ta da.ogg")

    def iniciar(self):
        pilas.avisar("Preciona la 'A' para ver la ayuda")
        f = pilas.fondos.Fondo("data/imagenes/fondos/juego.jpg")
        self.iniciar_actores()
        self.iniciar_musica()
        self.pulsa_tecla.conectar(self.cuando_pulsa_tecla)

    def iniciar_actores(self):
        def subir_nivel(a,n):
            n.eliminar()
            self.nivel = self.nivel + 1
            cartel  = pilas.actores.Texto("Iniciando nivel %s"%self.nivel)
            pilas.mundo.agregar_tarea(1.5,cartel.eliminar)
        #Puntos y vidas
        self.texto_pts = pilas.actores.Texto("Puntos:",fuente="data/tipografias/American Captain.ttf",x=130,y=320)
        self.texto_pts.color = pilas.colores.blanco
        self.puntos = pilas.actores.Puntaje(y=320,x=230,color=pilas.colores.blanco)
        self.vidas = ContadorDeVidas(3)
        #DADO
        self.dado=Dado(x=-340)
        self.dado.conectar_presionado(self.tirando_dado)
        # Cartel llegada
        self.meta = pilas.actores.Texto("Llegada", fuente="data/tipografias/American Captain.ttf",x=casillero_x[-1],y=casillero_y[-1])
        self.meta.color = pilas.colores.azuloscuro
        self.meta.escala=1.5
        #Paso de nivel
        cartel  = pilas.actores.Texto("Iniciando nivel 1")
        pilas.mundo.agregar_tarea(1.5,cartel.eliminar)
        # figura principal
        self.actor = pilas.actores.Actor("data/imagenes/elems_tablero/actor.png",x=casillero_x[0],y=casillero_y[0])
        pilas.mundo.agregar_tarea(2,self.chequear)
        #self.niveles = pilas.grupo.Grupo() NO LE HACE CASO
        #n2 = pilas.actores.Texto("N2",x=casillero_x[13],y=casillero_y[13])
        #self.niveles.append(n2)
        #n3 = pilas.actores.Texto("N3",x=casillero_x[25],y=casillero_y[25])
        #self.niveles.append(n3)
        #pilas.mundo.colisiones.agregar(self.actor,self.niveles,subir_nivel)

    def tirando_dado(self):
        n = self.dado.tirar()
        self.dado.desactivar()
        p1 = self.pos
        self.pos = self.pos + n
        #Solucion 2 para nivel
        if (self.pos>=13):
            if self.pos<25:
                self.nivel = 2
                if not self.inf2:
                    cartel  = pilas.actores.Texto("Iniciando nivel 2")
                    pilas.mundo.agregar_tarea(1.5,cartel.eliminar)
                    self.inf2=True
            else:
                self.nivel = 3
                if not self.inf3:
                    cartel  = pilas.actores.Texto("Iniciando nivel 3")
                    pilas.mundo.agregar_tarea(1.5,cartel.eliminar)
                    self.inf3=True
        if self.pos>38 :
            self.pos = 38
        p2 = self.pos + 1
        self.actor.x = casillero_x[p1:p2],1
        self.actor.y = casillero_y[p1:p2],1
        if self.pos == 38 :
            self.nivel = 'Finalizado'
            self.sonido_llegada.reproducir()
            self.terminar_juego()
        else:
            pilas.mundo.agregar_tarea(1.3,self.ver_colisiones)

    def iniciar_desafio(self):
        if self.nivel ==1:
            n = random.choice([1,2])
            if n==1:
                pilas.almacenar_escena(minijuego_numeros())
            else:
                pilas.almacenar_escena(minijuego_animales(self.nivel))
        else:
            pilas.almacenar_escena(minijuego_animales(self.nivel))
    def retroceder(self, cant = 0):
        self.pos = self.pos - cant
        self.actor.x = casillero_x[self.pos]
        self.actor.y = casillero_y[self.pos]
        pilas.mundo.agregar_tarea(1,self.ver_colisiones)

    def ver_colisiones(self):
        if self.pos in lista_desafios:
            self.iniciar_desafio()
        elif self.pos in lista_ret2:
            self.retroceder(2)
        elif self.pos in lista_ret4:
            self.retroceder(4)
        elif self.pos in lista_preg:
            self.hacer_pregunta()
        elif self.pos in lista_av2:
            self.retroceder(-2)
        elif self.pos in lista_av4:
            self.retroceder(-4)
        pilas.mundo.agregar_tarea(0.5,self.dado.activar)


    def iniciar_musica(self):
        f = open("data/estado_musica.txt",'rb')
        est = pickle.load(f)
        f.close()
        self.b_sonido = Sonido(y=320,x=430,musica=self.musica,estado = est)
        if est : self.musica.reproducir()

    def cuando_pulsa_tecla(self, evento):
        if evento.texto == 'a':
            ver_ayuda()
        elif evento.texto =='p':
            pilas.escena.pausar()
        elif evento.texto =='t':
            self.terminar_juego()
       # elif evento.texto=='m':
        #    self.hacer_pregunta()


    def chequear(self):
        # Ver y actualizar puntaje
        try:
            archivo = open("data/ultimo_puntaje.txt",'rb')
            n = pickle.load(archivo)
            archivo.close()
            import os
            os.remove("data/ultimo_puntaje.txt")
            if (n<0) :
                self.vidas.quitar_una_vida()
            else :
                self.puntos.escala = [2,1]
                self.puntos.aumentar(n)
        except:
            pass
            #pilas.avisar("Chequeando",0.5)
        # ver vidas
        if not self.vidas.le_quedan_vidas():
            self.terminar_juego("Perdiste")
        # si termino finaliza tarea
        if not self.fin:
            return True
        else:
            return False


    def guardar_datos(self):
        #Se abre y recopila informacion
        try :
            archivo = open("data/historial.txt",'rb')
            dic = pickle.load(archivo)
            archivo.close()
        except IOError :
            dic ={}
        #Se agrega la nueva info
        if self.nivel=='Finalizado':
            clave=self.nombre+' '+self.nivel
        else:
            clave = self.nombre + ' (nivel %s)'%self.nivel
        dic[clave]=str(self.puntos_fin)
        # Se guarda de nuevo en el archivo, reemplazandolo
        archivo = open("data/historial.txt",'wb')
        pickle.dump(dic,archivo)
        archivo.close()
        cerrar()

    def terminar_juego(self,cartel="Llegaste!!"):
        self.fin = True
        c = pilas.actores.Texto(cartel,y=150,fuente="data/tipografias/Insanibu.ttf")
        c.escala = 2
        c.color = pilas.colores.rojo
        self.puntos_fin = self.puntos.obtener()
        self.dado.eliminar()
        c1 = pilas.actores.Texto("Lograste %s puntos. \n Deseas guardar tu partida?"% self.puntos_fin,fuente="data/tipografias/Insanibu.ttf",y=50)
        c1.color = pilas.colores.amarillo
        opciones = [("Si, guardar y salir",self.guardar_datos),("No, salir sin guardar",cerrar)]
        self.menu = pilas.actores.Menu(opciones,fuente="data/tipografias/Insanibu.ttf",color_normal = pilas.colores.blanco,
                                       color_resaltado=pilas.colores.rojo, y=-100)


    def hacer_pregunta(self):
        #actor interactuante
        actor = pilas.actores.Actor("data/imagenes/varios/actor.png",x=700)
        actor.x = [-315]
        # Preparando informacion pregunta
        dial = pilas.actores.Dialogo()
        # Operadores y operando
        n1 = random.randint(1,11)
        n2 = random.randint(1,11)
        signo = random.choice(['+','-'])
        # Resultado (controlamos que sea positivo)
        if signo=='+':
            res = str(n1+n2)
        else:
            if n1<n2:
                aux = n1
                n1 = n2
                n2 = aux
            res=str(n1-n2)

        #Creamos lista de respuestas posibles
        respuestas = []
        respuestas.append(res)
        cant = self.nivel + 2
        for i in range(cant):
            n = str(random.randrange(1,21))
            while n in respuestas :
                n = str(random.randrange(1,21))
            respuestas.append(n)
        respuestas.sort()
        pregunta = "Cuanto es %s %s %s ?"%(n1,signo,n2)
        def ver_respuesta(r):
            if r==res:
                pts = self.nivel*10
                tx ="Muy bien, sumas %s puntos" % pts
                self.puntos.aumentar(pts)
                self.puntos.escala = [2,1]
                self.sonido_bien.reproducir()
            else:
                tx = "Que lastima! era %s"%res
                self.sonido_fallo.reproducir()
            actor.decir(tx)
            dial.iniciar()
            def irse():
                actor.x = [-600]
                actor.y = [300]
            pilas.mundo.agregar_tarea(1,irse)
        dial.elegir(actor,pregunta,respuestas,ver_respuesta)

        pilas.mundo.agregar_tarea(2,dial.iniciar)

'''pilas.iniciar(1024,712,titulo="La oca")       	
pilas.mundo.motor.alto_original = 712
pilas.mundo.motor.ancho_original = 1024
m = pilas.sonidos.cargar("data/musica/Sneaky_Adventure.ogg")
pilas.cambiar_escena(Juego())
pilas.ejecutar()'''
