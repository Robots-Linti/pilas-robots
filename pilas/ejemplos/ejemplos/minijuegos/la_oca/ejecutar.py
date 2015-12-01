import pilas
import escena_menu

pilas.iniciar(1024,712,titulo="La oca")
         	
pilas.mundo.motor.alto_original = 712
pilas.mundo.motor.ancho_original = 1024
pilas.cambiar_escena(escena_menu.Menu())

pilas.ejecutar()
