import pilas

class ContadorDeVidas:

    def __init__(self, cantidad_de_vidas):
        self.crear_texto()
        self.cantidad_de_vidas = cantidad_de_vidas
        self.vidas = [pilas.actores.Actor("data/imagenes/varios/vida.png") for x in range(cantidad_de_vidas)]

        for indice, vida in enumerate(self.vidas):
            vida.aprender(pilas.habilidades.PuedeExplotar)
            vida.x = -200 + indice * 30
            vida.arriba = 330

    def crear_texto(self):
        "Genera el texto que dice 'vidas'"
        self.texto = pilas.actores.Texto("Vidas:",fuente="data/tipografias/American Captain.ttf")
        self.texto.color = pilas.colores.blanco
        self.texto.magnitud = 20
        self.texto.izquierda = -300
        self.texto.arriba = 330

    def le_quedan_vidas(self):
        return self.cantidad_de_vidas > 0

    def quitar_una_vida(self):
        self.cantidad_de_vidas -= 1
        vida = self.vidas.pop()
        vida.eliminar()

