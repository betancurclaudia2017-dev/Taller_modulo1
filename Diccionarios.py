Carro = {
    "Marca" : "Toyota",
    "Modelo" : "Corolla",
    "Año" : "2020",
    "Colores" : ["Rojo", "verde", "Amarillo"],
    "Electrico" : False
}

Carro["color"] = "Rojo"
print(Carro)
print(len(Carro))
print(Carro["Colores"])
print(type(Carro))
fruta = dict(Nombre = "Manzana", Color = "Rojo", Sabor = "Dulce", Valor = 2500)
print(fruta)
X = fruta ["Nombre"]
print(X)
print(fruta.keys())
fruta["Valor"] = 3000 
print(fruta)
"""
·Metodos de diccionarios
CLEAR()
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)
·SIRVE PARA:
Borra todas las claves y valores del diccionario, No elimina la variable, solo su contenido
-------------------------------------------------------------------------------------------
·COPY()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)

·PARA QUE SIRVE?
Para crear una copia del diccionario Original 
----------------------------------------------

·FROMKEYS()
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
·PARA QUE SIRVE?

Para crecar un diccionario nuevo, a partir de una de las listas claves, asignandoles a todas el mismo valor
-----------------------------------------------------------------------------------------------------------

·GET()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)
PARA QUE SIRVE?
Sirve para obtener el valor de una clave, sin que el programa falle si la clave no existe
-----------------------------------------------------------------------------------------

·ITEMS()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)
·PARA QUE SIRVE?
Sirve para obtener todos los pares clave-valor del dicionario en forma de tuplas
--------------------------------------------------------------------------------

·KEYS()


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)
·PARA QUE SIRVE?
Sirve oara obtener las claves del diccionario 
---------------------------------------------

·POP()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

·PARA QUE SIRVE?
Para eliminar una clave y al mismo tiempo devolver su valor
------------------------------------------------------------
·POPITEM()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)

·PARA QUE SIRVE?
Sirve para eliminar y devolver el ultimo par agregado al diccionario
----------------------------------------------------------------------
·SETDEAFULT()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

PARA QUE SRIVE?
·Para obtener el valor de una clave y, si no existe, crearla con un valor por defecto
-------------------------------------------------------------------------------------
UPDATE()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

·PARA QUE SIRVE? 
Sirve para agregar nuevos elementos o actualizar los que ya existe usando otro diccionario
-------------------------------------------------------------------------------------------
·VALUES()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)

·PARA QUE SIRVE ?
PARA OBTENER TODOS LOS VALORES DEL DICCIONARIO.


"""




