# -*- encoding: utf-8 -*-
# pilas engine - a video game framework.
#
# copyright 2010 - hugo ruscitti
# license: lgplv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# website - http://www.pilas-engine.com.ar

import pilas
import random


class Piezas(pilas.escenas.Normal):
    """Representa la escena de rompecabezas.

    La escena comienza con una imagen que se descompone en muchos
    actores Pieza.
    """

    def __init__(self, ruta_a_la_imagen="ejemplos/data/piezas.png", filas=2, columnas=2):
        pilas.actores.eliminar_a_todos()
        pilas.escenas.Normal.__init__(self, pilas.colores.gris_oscuro)
        grilla = pilas.imagenes.Grilla(ruta_a_la_imagen, columnas, filas)
        self.crear_piezas(grilla, filas, columnas)
        self.pieza_en_movimiento = None

        pilas.eventos.click_de_mouse.conectar(self.al_hacer_click)
        pilas.eventos.termina_click.connect(self.al_soltar_el_click)
        pilas.eventos.mueve_mouse.connect(self.al_mover_el_mouse)

    def crear_piezas(self, grilla, filas, columnas):
        "Genera todas las piezas en base al tamaño del constructor."
        self.piezas = []
        self.grupos = {}

        for x in range(filas * columnas):
            self.grupos[x] = set([x])
            pieza = Pieza(self, grilla, x, filas, columnas)
            self.piezas.append(pieza)
            pieza.x = random.randint(-200, 200)
            pieza.y = random.randint(-200, 200)


    def al_hacer_click(self, **kv):
        "Atiente cualquier click que realice el usuario en la pantalla."
        pieza_debajo_de_mouse = pilas.actores.obtener_actor_en(kv['x'], kv['y'])

        if pieza_debajo_de_mouse and isinstance(pieza_debajo_de_mouse, Pieza):
            self.pieza_en_movimiento = pieza_debajo_de_mouse

    def al_soltar_el_click(self, **kv):
        if self.pieza_en_movimiento:
            self.pieza_en_movimiento.soltar_todas_las_piezas_del_grupo()
            self.pieza_en_movimiento = None

    def al_mover_el_mouse(self, **kv):
        if self.pieza_en_movimiento:
            self.pieza_en_movimiento.x += kv['dx']
            self.pieza_en_movimiento.y += kv['dy']
            
    def conectar(self, pieza_a, pieza_b):
        a = pieza_a.numero
        b = pieza_b.numero
  
        if a in self.grupos[b]:
            #Evita contectar mas de una vez a dos piezas.
            return

        """Inicialmente comienzo con::


            0: [0, 1, 2]
            1: [0, 1, 2]
            2: [0, 1, 2]
            3: [3]

        ¿y si conecto la pieza 3 con la 2?

        - tendría que obtener todas las piezas que conoce 2.
        
        - iterar en ese grupo y decirle a cada pieza que sume a 3 en su grupo::

            0: [0, 1, 2, 3]
            1: [0, 1, 2, 3]
            2: [0, 1, 2, 3]

        - luego solo me falta tomar a uno de esos grupos actualizados
          y decirle a 3 que ese será su grupo::

            3: [0, 1, 2, 3]
        """
        
        grupo_a_pertenecer = set(self.grupos[a])

        for pieza in grupo_a_pertenecer:
            self.grupos[pieza] = self.grupos[pieza].union(self.grupos[b])

        self.grupos[b] = self.grupos[b].union(grupo_a_pertenecer)
        
class Pieza(pilas.actores.Animado):
    """Representa una pieza del rompecabezas.

    Esta pieza se puede arrastrar con el mouse y cuando se suelta
    intentará conectarse con las demás."""

    def __init__(self, escena_padre, grilla, cuadro, filas, columnas):
        pilas.actores.Animado.__init__(self, grilla)

        self.numero = cuadro

        self.asignar_numero_de_piezas_laterales(cuadro, columnas)

        self.definir_cuadro(cuadro)

        self.radio_de_colision = self.obtener_ancho() / 2 + 10
        self.escena_padre = escena_padre
        self.piezas_conectadas = []

    def asignar_numero_de_piezas_laterales(self, cuadro, columnas):
        "Guarda el numero de las piezas que se pueden conectar en sus bordes."
        self.numero_arriba = cuadro - columnas
        self.numero_abajo = cuadro + columnas

        if cuadro % columnas == 0:
            self.numero_izquierda = -1
        else:
            self.numero_izquierda = cuadro - 1

        if cuadro % columnas == columnas -1:
            self.numero_derecha = -1
        else:
            self.numero_derecha = cuadro + 1

    def soltar_todas_las_piezas_del_grupo(self):
        for numero in self.escena_padre.grupos[self.numero]:
            pieza = self.escena_padre.piezas[numero]
            pieza.soltar()


    def soltar(self):
        # Busca todas las colisiones entre esta pieza
        # que se suelta y todas las demás.
        colisiones = pilas.colisiones.obtener_colisiones(self, self.escena_padre.piezas)

        for x in colisiones:
            self.intentar_conectarse_a(x)

    def se_pueden_conectar_los_bordes(self, borde1, borde2):
        return pilas.utils.distancia(borde1, borde2) < 12

    def intentar_conectarse_a(self, otra):
        "Intenta vincular dos piezas, siempre y cuando coincidan en sus bordes."

        # Intenta conectar los bordes laterales
        if self.numero_derecha == otra.numero:
            if self.se_pueden_conectar_los_bordes(self.derecha, otra.izquierda):
                otra.izquierda = self.derecha
                otra.arriba = self.arriba

                self.conectar_con(otra)
        elif self.numero_izquierda == otra.numero:
            if self.se_pueden_conectar_los_bordes(self.izquierda, otra.derecha):
                otra.derecha = self.izquierda
                otra.arriba = self.arriba

                self.conectar_con(otra)

        # Intenta conectar los bordes superior e inferior
        if self.numero_abajo == otra.numero:
            if self.se_pueden_conectar_los_bordes(self.abajo, otra.arriba):
                otra.arriba = self.abajo
                otra.izquierda = self.izquierda
        
                self.conectar_con(otra)
        elif self.numero_arriba == otra.numero:
            if self.se_pueden_conectar_los_bordes(self.arriba, otra.abajo):
                otra.abajo = self.arriba
                otra.izquierda = self.izquierda

                self.conectar_con(otra)


    def conectar_con(self, otra_pieza):
        self.escena_padre.conectar(self, otra_pieza)


    def __repr__(self):
        return "<<Pieza %d>>" %(self.animacion.obtener_cuadro())


    def set_x(self, x):
        "A diferencia de los actores normales, las piezas tienen que mover a todo su grupo."
        dx = x - self.x

        for numero in self.escena_padre.grupos[self.numero]:
            pieza = self.escena_padre.piezas[numero]
            pieza.SetX(pieza.x + dx)

    def set_y(self, y):
        "A diferencia de los actores normales, las piezas tienen que mover a todo su grupo."
        dy = y - self.y

        for numero in self.escena_padre.grupos[self.numero]:
            pieza = self.escena_padre.piezas[numero]
            pieza.SetY(-pieza.y - dy)

    def get_x(self):
        x, y = self.GetPosition()
        return x

    def get_y(self):
        x, y = self.GetPosition()
        return -y

    x = property(get_x, set_x, doc="Define la posición horizontal.")
    y = property(get_y, set_y, doc="Define la posición vertical.")
