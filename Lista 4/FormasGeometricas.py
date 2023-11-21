import math

class FormasGeometricas:
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass


class Retangulo(FormasGeometricas):
    def __init__(self, base, altura) -> None:
        self.__base = base
        self.__altura = altura

    def calcularArea(self):
        area = self.__base * self.__altura
        return area
    
    def calcularPerimetro(self):
        perimetro = (2*self.__base) + (2*self.__altura)
        return perimetro

class Triangulo(FormasGeometricas):
    def __init__(self, base, altura) -> None:
        self.__base = base
        self.__altura = altura

    def calcularArea(self):
        area = (self.__altura * self.__base)/2
        return area
    
    def calcularPerimetro(self):
        #supondo que seja um triangulo equilátero
        perimetro = 3*self.__base
        return perimetro

class Circulo(FormasGeometricas):
    def __init__(self, raio) -> None:
        self.__raio = raio

    def calcularArea(self):
        area = math.pi*(self.__raio**2)
        return area

    def calcularPerimetro(self):
        perimetro = 2*math.pi*self.__raio
        return perimetro
    
circulo = Circulo(2)
retangulo = Retangulo(4,2)
triangulo = Triangulo(2,2)

print('Área do círculo:', circulo.calcularArea(), '\Circunferência do círculo:', circulo.calcularPerimetro())
print('Área do retangulo:', retangulo.calcularArea(), '\nPerímetro do retangulo:', retangulo.calcularPerimetro())
print('Área do triangulo:', triangulo.calcularArea(), '\nPerímetro do triangulo:', triangulo.calcularPerimetro())