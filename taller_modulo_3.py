from __future__ import annotations
import json
import uuid
from enum import Enum

class consolePlatform(Enum):
    PC = 1
    PLAYSTATION = 2
    XBOX = 3 
    NINTENDO = 4
    NOT_DEFINED = 5


class storage_entry():
    __slots__ = ("code","game")

    storage:dict={}

    def __init__(self, *, code:str, game:VideoGame) -> None:
        self.code = code
        self.game = game

        storage_entry.storage.setdefault(code, game)

    @staticmethod
    def print_storage():
        dic = storage_entry.storage
        
        if not dic:
            print("The storage is empty!!")
            return

        storage_serializado = {}
        
        for clave, juego in dic.items():
            storage_serializado[clave] = {
                "name": juego.name,
                "platform": str(juego.platform.name),
                "price": juego.price,
                "units": juego.units
            }
        
        print(json.dumps(storage_serializado, indent=4))

                
    
    @staticmethod
    def newRegister():
        name = storage_entry._def_name()
        platform = storage_entry._def_platform()
        price =storage_entry._def_price()
        units = storage_entry._def_units()

        new_video_game = VideoGame(name=name, platform=platform, price=price, units=units)
        code = str(uuid.uuid4())

        storage_entry(code=code, game=new_video_game)

    @staticmethod
    def _def_name()->str:
        name = input("Please submit the name of the videogame: ")
        while name.strip() == "":
            name = input("Name is not valid, try again: ")
        return name
    
    @staticmethod
    def _def_platform()->consolePlatform:
        i = 1
        print("Please select the platform:\n")
        for estado in consolePlatform:
            if estado.name != consolePlatform.NOT_DEFINED:
                print(i, estado.name)
                i += 1
        try:
            platform = int(input("Please select the number: "))
        except ValueError:
            print("Error: You must submit a valid number (e.g., 2)")
        while platform not in [1,2,3,4]:
            platform = input("Number selected is not valid, please try again: ")
        for estado in consolePlatform:
            if platform == estado.value:
                platform = estado
        return platform
    
    @staticmethod
    def _def_price() -> float:
        while True:
            try:
                entrada = input("How much does the video game cost in dollars?(Dollars.cents): ")
                price = float(entrada)
                
                if price >= 0.1:
                    return price
                    
                print("Error: The price must be 0.1 or above")
                
            except ValueError:
                print("Error: You must submit a valid number (e.g., 12.99)")

    @staticmethod
    def _def_units()->int:
        while True:
            try:
                entrada = input("How many units does video game have?: ")
                price = int(entrada)
                
                if price >= 1:
                    return price
                    
                print("Error: The units must above 0")
                
            except ValueError:
                print("Error: You must submit a valid number (e.g., 2)")

        


class VideoGame():
    __slots__ = ("name","platform","price","units",)

    def __init__(self,*, name:str, platform:consolePlatform, price:float, units:int) -> None:
        self.name = name
        self.platform = consolePlatform
        self.price = price
        self.units = units

storage_entry.newRegister()

MENU = """
===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por código
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir
"""


# @staticmethod
#     def _def_platform() -> consolePlatform:
#         # 1. Filtramos las plataformas válidas (excluyendo NOT_DEFINED)
#         opciones_validas = [p for p in consolePlatform if p != consolePlatform.NOT_DEFINED]

#         while True:
#             print("\nPlease select the platform:\n")
#             # Imprime el menú automáticamente usando el índice de la lista (+1)
#             for indice, estado in enumerate(opciones_validas, start=1):
#                 print(f"{indice}. {estado.name}")
            
#             try:
#                 seleccion = int(input("\nPlease select the number: "))
                
#                 # Validamos si el número está dentro del rango de la lista
#                 if 1 <= seleccion <= len(opciones_validas):
#                     # Retornamos directamente el miembro del Enum usando el índice (restamos 1)
#                     return opciones_validas[seleccion - 1]
                
#                 print(f"Error: Number must be between 1 and {len(opciones_validas)}.")
                
#             except ValueError:
#                 print("Error: You must submit a valid number (e.g., 2)")
# @staticmethod
#     def print_storage():
#         dic = storage_entry.storage
        
#         if not dic:
#             print("The storage is empty!!")
#             return

#         storage_serializado = {}
        
#         for clave, juego in dic.items():
#             storage_serializado[clave] = {
#                 "name": juego.name,
#                 # .name ya devuelve un string (ej: "SWITCH")
#                 # Si prefieres el valor numérico (ej: 1), usa juego.platform.value
#                 "platform": juego.platform.name, 
#                 "price": juego.price,
#                 "units": juego.units
#             }
        
#         print(json.dumps(storage_serializado, indent=4))