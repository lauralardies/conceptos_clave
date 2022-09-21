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