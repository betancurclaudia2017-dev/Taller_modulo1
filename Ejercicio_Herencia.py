##Crear una clase padre (Vehiculo) y tres clases hijas (Carro)(Moto)(Barco)

###class Vehiculo:
    #def __init__(self, Marca ):
        #self.Marca = Marca

   # def Velocidad(self):
        #print("")

#class Carro(Vehiculo):  

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod

    def Area(self):
        pass
class cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado*self.lado
    
c = cuadrado(7)
print(c.Area())
    
"""
Crear una clase abstracta empledo, metodo abtracto calcular salario 
sub clase desarrollador 
"""

from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_Salario(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, programas):
        self.programas = programas


P = Desarrollador("Python")
print("El programada del desarrollador se llama: ", P.programas()) 