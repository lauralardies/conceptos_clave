from punto import Punto
from rectangulo import Rectangulo

print("---------------------------------------------")
print("------------ EJERCICIO DE PUNTOS ------------")
print("---------------------------------------------")

x = int(input("Selecciona la coordenada X de tu punto: "))
y = int(input("Selecciona la coordenada Y de tu punto: "))

if x == "":
    x = 0
if y == "":
    y = 0

punto = Punto(x, y)
punto.cuadrante()

x2 = int(input("Selecciona la coordenada X de tu nuevo punto para crear un vector con el punto anterior: "))
y2 = int(input("Selecciona la coordenada Y de tu nuevo punto para crear un vector con el punto anterior: "))

if x2 == "":
    x2 = 0
if y2 == "":
    y2 = 0

punto.vector(x2, y2)

