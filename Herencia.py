class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def Hacer_Sonido(self):
        print("Hacer sonido Genèrico")
class Perro(Animal):
    def Hacer_Sonido(self):
        return("wauu wauu")

class Gato(Animal):
    def __init__(self, nombre, Edad):
        super().__init__(nombre)
        self.Edad  = Edad
    
    def Hacer_Sonido(self):
        return "Miauu Miauu"

P = Perro("Trosky")
print(f"{P.nombre} dice {P.Hacer_Sonido()}")
A = Animal("Laika")
print(f"{A.nombre} dice", P.Hacer_Sonido())
A.Hacer_Sonido()

G = Gato("Mirringo", 5)
print(G.Edad)
print(G.Hacer_Sonido())