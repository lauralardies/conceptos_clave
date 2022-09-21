from punto import Punto

class Rectangulo():

    def __init__(self, inicio, final) -> None:
        self.inicio = inicio
        self.final = final

    def base(self):
        vector = Punto.vector()
