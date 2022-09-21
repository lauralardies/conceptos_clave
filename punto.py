import math

class Punto():

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.punto = "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def print_punto(self):
        return print(self.punto)

    def cuadrante(self):
        if self.x == 0:
            if self.y == 0:
                print("El punto es el centro de coordenadas.")
            if self.y != 0:
                print("El punto está sobre el eje Y.")
        if self.y == 0:
            if self.x != 0:
                print("El punto está sobre el eje X.")
        else:
            if self.y > 0 and self.x > 0:
                print("El punto pertenece al primer cuadrante.")
            if self.y < 0 and self.x > 0:
                print("El punto pertenece al segundo cuadrante.")
            if self.y < 0 and self.x < 0:
                print("El punto pertenece al tercer cuadrante.")
            if self.y > 0 and self.x < 0:
                print("El punto pertenece al cuarto cuadrante.")
    
    def vector(self, coordenada_x, coordenada_y):
        vector_x = coordenada_x - self.x
        vector_y = coordenada_y - self.y
        return print("(" + str(vector_x) + ", " + str(vector_y) + ")")  

    def distancia(self, coordenada_x, coordenada_y):
        dist = math.sqrt(((coordenada_x - self.x)**2) + ((coordenada_y - self.y)**2))
        return print (dist)