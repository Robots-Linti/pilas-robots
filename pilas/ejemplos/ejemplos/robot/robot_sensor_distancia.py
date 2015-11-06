# -*- encoding: utf-8 -*-

# Importar la librería
import pilas

#Iniciar
pilas.iniciar()


# Definición de los actores
b = pilas.actores.Board("/dev/tty/USB0")
r = pilas.actores.Robot(b, 1)
m = pilas.actores.Mono()


# Posiciones de los actores
r.x = 11
r.y = -30
m.x = 15
m.y = 140

# Avance del Robot
r.forward(20)
while  r.ping() > 30 :
  #  pilas.avisar("Distancia entre el Robot y el Mono:", r.ping())
    pilas.avisar("Distancia entre el Robot y el Mono: " +  str(r.ping()))
# Se acerca al Mono
m.decir("Cuidado!!!!!")

# Detener el Robot
r.stop()
print r.getName()

pilas.ejecutar()
