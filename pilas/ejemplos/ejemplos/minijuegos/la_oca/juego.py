import pilas
from escena_menu import Menu

pilas.iniciar(1024,712,titulo="La oca")
         	
pilas.mundo.motor.alto_original = 712
pilas.mundo.motor.ancho_original = 1024
pilas.cambiar_escena(Menu())

pilas.ejecutar()
