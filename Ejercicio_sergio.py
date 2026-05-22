class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre #Encapsulamiento (privado)
    
    def Hablar(self):
        print("La persona esta hablando")

    def vestirse(self):
        print("La persona se esta vistiendo")

    def get_nombre(self):   #Nos perminte acceder a la variable
        return self.__nombre
    
class Hombre(Persona): #La clase Hombre hereda de Persona 
    pass

    def vestirse(self):
        print("El hombre se viste con pantalon y camisa")

class Mujer(Persona):
    pass
    def vestirse(self):
        print("La mujer se viste con vestido y tacones") #Polimorfismo, Usamos el metodo Vestir pero ambos de viszten de forma difernte


P1 = Hombre("Juan")
P2 = Mujer("Ana")

P1.Hablar()
P1.vestirse()

P2.Hablar()
P2.vestirse()

"""
Herencia: 
Es cuando una sub clase hereda de la clase principal (Metodos y atributos)

Abstracciòn:
Es decir Hablar o vestirse solo lo que hace no como lo hace

Encapsulamiento
Se usa para proteger los datos para que no se modifiquen direcctamente 

Polimorfismo:
Es cuando un mismo metodo hace clsas diferentes segun el objeto 


"""



