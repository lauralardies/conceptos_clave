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

print("--------------------------------------------")
print("--------- EJERCICIO DEL RECTÁNGULO ---------")
print("--------------------------------------------")

inicio_x = int(input("Selecciona la coordenada X de tu punto inicial de la diagonal del rectángulo: "))
inicio_y = int(input("Selecciona la coordenada Y de tu punto inicial de la diagonal del rectángulo: "))

if inicio_x == "":
    inicio_x = 0
if inicio_y == "":
    inicio_y = 0

final_x = int(input("Selecciona la coordenada X de tu punto final de la diagonal del rectángulo: "))
final_y = int(input("Selecciona la coordenada Y de tu punto final de la diagonal del rectángulo: "))

if final_x == "":
    final_x = 0
if final_y == "":
    final_y = 0

rectangulo = Rectangulo(inicio_x, inicio_y, final_x, final_y)
rectangulo.area()