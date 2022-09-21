# conceptos_clave

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/conceptos_clave)
https://github.com/lauralardies/conceptos_clave

## Código clase Punto
```
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
        return print("Vector (" + str(vector_x) + ", " + str(vector_y) + ")")   
        
    def distancia(self, coordenada_x, coordenada_y):
        dist = math.sqrt(((coordenada_x - self.x)**2) + ((coordenada_y - self.y)**2))
        return print (dist)
```
## Código clase Rectángulo
```
import turtle

class Rectangulo():

    def __init__(self, inicio_x, inicio_y, final_x, final_y) -> None:
        self.inicio_x = inicio_x
        self.inicio_y = inicio_y
        self.inicio = "(" + str(self.inicio_x) + ", " + str(self.inicio_y) + ")"
        self.final_x = final_x
        self.final_y = final_y
        self.final = "(" + str(self.final_x) + ", " + str(self.final_y) + ")"
        self.vector_x = self.final_x - self.inicio_x
        self.vector_y = self.final_y - self.inicio_y

    def base(self):
        return print(self.vector_x)
    
    def altura(self):
        return print(self.vector_y)

    def area(self):
        base = self.vector_x
        altura = self.vector_y

        return print(base * altura)
    
    def dibujar_rectangulo(self):
        turtle.forward(self.vector_x)
        turtle.left(90)
        turtle.forward(self.vector_y)
        turtle.left(90)
        turtle.forward(self.vector_x)
        turtle.left(90)
        turtle.forward(self.vector_y)
        turtle.left(90)
        turtle.done()
```
## Código Main
```
from punto import Punto
from rectangulo import Rectangulo

print("---------------------------------------------")
print("-------------- EXPERIMENTACIÓN --------------")
print("---------------------------------------------")

x1 = int(input("Selecciona la coordenada X de tu punto A: "))
y1 = int(input("Selecciona la coordenada Y de tu punto A: "))
A = Punto(x1, y1)
A.print_punto()
A.cuadrante()

x2 = int(input("Selecciona la coordenada X de tu punto B: "))
y2 = int(input("Selecciona la coordenada Y de tu punto B: "))
B = Punto(x2, y2)
B.print_punto()
B.cuadrante()

x3 = int(input("Selecciona la coordenada X de tu punto C: "))
y3 = int(input("Selecciona la coordenada Y de tu punto C: "))
C = Punto(x3, y3)
C.print_punto()
C.cuadrante()

x4 = int(input("Selecciona la coordenada X de tu punto D: "))
y4 = int(input("Selecciona la coordenada Y de tu punto D: "))
D = Punto(x4, y4)
D.print_punto()
D.cuadrante()

print("Vector AB:")
A.vector(x2, y2)

print("Vector BA:")
B.vector(x1, y1)

print("Distancia de A a B:")
A.distancia(x2, y2)

print("Distancia de B a A:")
B.distancia(x1, y1)

rectangulo = Rectangulo(x1, y1, x2, y2)
rectangulo.dibujar_rectangulo()
rectangulo.base()
rectangulo.altura()
rectangulo.area()
```
