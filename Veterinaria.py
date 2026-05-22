from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar_nombre(self):
        pass

class Veterinario(Persona):
    def mostrar_nombre(self):
        print(f"Veterinario {self.nombre}")

    def atender(self):
        return f"{self.nombre} Esta atendiento a una mascota"

class Mascota(Persona):
    def __init__(self, nombre, especie):
        super().__init__(nombre)
        self.especie = especie

    def mostrar_nombre(self):
        return self.nombre

    def mostrar_info(self):
        return f"Nombre {self.nombre} Especie {self.especie}"
    
class Consulta:
    def __init__(self, mascota, motivo):
        self.mascota = mascota
        self.motivo = motivo 

    def mostrar_consulta(self):
        return f"Consulta para: {self.mascota.nombre} {self.mascota.especie}"

        
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []

    def Agregar_Mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        print(f"Cliente: {self.nombre} ")
        for mascota in self.mascotas:
            print(mascota.mostrar_info())

cliente = Cliente("Ana")
mascota1 = Mascota("Trosky", "Canino")
mascota2 = Mascota("Michin", "Canino")

cliente.Agregar_Mascota(mascota1)
cliente.Agregar_Mascota(mascota2)
veterinario1 = Veterinario("jhon Garcia")
consulta1 = Consulta(mascota1, "Vacunaciòn")
cliente.mostrar_mascotas()

print(veterinario1.atender())
print(consulta1.mostrar_consulta())

    



