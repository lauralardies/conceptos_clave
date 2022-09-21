from punto import Punto

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
        return self.vector_x
    
    def altura(self):
        return self.vector_y

    def area(self):
        base = self.vector_x
        altura = self.vector_y

        return print(base * altura)