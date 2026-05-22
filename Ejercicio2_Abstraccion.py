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