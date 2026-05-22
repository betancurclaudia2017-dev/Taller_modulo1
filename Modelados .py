"""
RELACIÒN ASOCIACIÒN 

class Cliente:
    def __init__(self, nombre):
    self.nombre = nombre

class Pedido:
    def __init__(self, cliente):
    self.cliente = cliente

#INSTANCIAS 

C1 = Cliente("Pedro")

P1 = Pedido(C1)
"""
"""
#RELACIÒN AGREGACION

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
class restaurante:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleado.append(empleado)


        
e = Empleado("Roberto")

r = restaurante()

r.agregar_empleado(e)
"""

##Relaciòn de composiciòn 
"""
class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre 
        self.precio = precio

class Pedido:
    def __init__(self):
        self.platos = []
    def agregar_plato(self, nombre, precio):
        plato = Plato(nombre, precio)
        self.platos.append(plato)
#plato = Plato("Bandeja paisa", 35000)(ESTO NO DEBE HACERCE)

pedido = Pedido()
pedido.agregar_plato("Sancocho", 30000)

"""
from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    @abstractmethod

    def calcular_salario(self):
        pass
class Mesero(Empleado):
    def calcular_salario(self):
        return 1000
    
class chef(Empleado):
    def calcular_salario(self):
        return 2000
    

