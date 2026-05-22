from abc import ABC, abstractmethod

class trabajable(ABC):
    @abstractmethod

    def Trabajar(self):
        pass

class Empleado(ABC):
    def __init__(self, Nombre, Salario_base):
        self.Nombre = Nombre
        self.Salario_base = Salario_base

    @abstractmethod
    
    def Calcular_Salario(self):
        pass

class Gerente(Empleado, trabajable):
    def __init__(self, Nombre, Salario_base, Bono):
        super().__init__(Nombre, Salario_base)
        self.Bono = Bono
    
    def Calcular_Salario(self):
        return self.Salario_base + self.Bono
    
    def Trabajar(self):
        print(f"{self.Nombre}, Esta tallando los empleados")

class Desarrollador(Empleado, trabajable):
    def __init__(self, Nombre, Salario_base,lenguaje):
        super().__init__(Nombre, Salario_base)
        self.lenguaje = lenguaje

    def Calcular_Salario(self):
        return self.Salario_base
    
    def Trabajar(self):
        print(f"{self.Nombre}, Esta desarrolando en: {self.lenguaje}")

Empleados = [
    Gerente("Ana", 4000, 1000),
    Desarrollador("luis ", 3000, "python")

]

for Elemento in Empleados:
    Elemento.Trabajar()
    print("Salario", Elemento.Calcular_Salario)
    print("____________________")
    
