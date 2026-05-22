#


class perro:
    def __init__(self,nombre,raza, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad

        #getters
    def get_nombre(self):
        return self.__nombre
        
    def get_raza(self):
        return self.__raza
        
    def get_edad(self):
        return self.__edad
        
#setters
    def set_nombre(self,nombre):
        self.__nombre=nombre

    def set_raza(self,raza):
        self.__raza=raza

    def set_edad(self,edad):
        if edad > 0:
            self.__edad=edad
        else:
            ("La edad debe ser igual mayor a 0")

#Metodo para mostrar informaciòn

    def mostrar_informacion(self):
        print("nombre:", self.get_nombre())
        print("raza:", self.get_raza())
        print("edad:", self.get_edad())
        print("-----------------")
    
def main():
    perro1 = perro("max", "Jack rousell", 5)
    perro2 = perro("Susy", "Criollita", 10)
    perro3 = perro("Lupe", "Bravita", 11)
    perro1.mostrar_informacion()
    perro2.mostrar_informacion()
    perro3.mostrar_informacion()

    perro1.set_edad(6)
    print("La nueva edad del perro 1", perro1.get_edad())
    perro1.mostrar_informacion()

if __name__ == "__main__":  main()



##Ejercicio 2 

class Libro:
    def __init__(self, titulo, autor, isbn, precio):
        self.__titulo = titulo
        self.__autor = autor 
        self.__isbn = isbn
        self.__precio = precio 

##Getters
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor 
    def get_isbn(self):
        return self.__isbn
    def get_precio(self):
        return self.__precio
    
##setters
    def set_titulo(self, titulo):
        self__titulo = titulo
    def set_autor(self, autor):
        self.__autor = autor 
    def set_isbn(self, isbn):
        self .__isbn = isbn
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio 
        else:
            print("El valor del libro debe ser mayor a 0 ")

## ·Metodo para mostar informaciòn 
    def mostrar_info(self):
        print("titulo: ", self.get_titulo())
        print("autor: ", self.get_autor())
        print("isbn: ", self.get_isbn())
        print("precio: ", self.get_precio())
        print("-----------------")

##clase principal        
def main():
    libro1 = Libro("Python Basico", "Juan Perez ", 12345, 50000)
    libro2 = Libro("IA para todos ", "Ana Gomez ", 67890, 75000)
    libro3 = Libro("POO en python ", "Carlos Ruiz ", 11223, 60000)

    libro1.mostrar_info()
    libro2.mostrar_info()
    libro3.mostrar_info()

    libro1.set_precio(55000)
    print("Nuevo precio del libro 1 es de: ", libro1.get_precio())
    libro1.mostrar_info()
if __name__ == "__main__": main()

class producto:
    def __init__(self, codigo, nombre, precio, stok):
        self.__codigo  = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stok = stok

    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return  self.__nombre 
    def get_precio(self):
        return self.__precio
    def get_stok(self):
        return self.__stok
    
    def set_codigo(self, Nuevo_codigo):
        self.__codigo = Nuevo_codigo
    def set_nombre(self, Nuevo_nombre):
        self.__nombre = Nuevo_nombre
    def set_precio(self, Nuevo_precio):
        self.__precio = Nuevo_precio
    def set_stok(self, Nuevo_Stok):
        self.__stok = Nuevo_Stok  

    def mostrar_info(self):
        print(f"Codigo: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: $ {self.__precio}")
        print(f"Stok:  {self.__stok} unidades")

    
    def vender(self,cantidad):
        if cantidad <= self.__stok:
            self.__stok -= cantidad
            return True
        else:
            return False

class sistema_de_productos():
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("producto agendado exitosamente")

    def mostrar_producto(self):
        print("Lista de productos")
        print("-"*30)
        for producto in self.productos:
            producto.mostrar_info()

    def Buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.get_codigo() == codigo:
                return producto
        return None
    def Eliminar_producto(self, codigo):
        producto = self.Buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            print("Prodcuto eliminado exitosamente")
        else:
            ("Producto no encontrado")
    def actualizar_precio(self, codigo, Nuevo_precio):
        producto = self.Buscar_producto(codigo)
        if producto:
            producto.set_precio(Nuevo_precio)
            print("precio actualizado exitosamente")
        else:
            print("Prodcuto no encontrado")

    def actualizar_stok(self, codigo, Nuevo_stok):
        producto = self.buscar_producto(codigo)
        if producto:
            producto.set_stok(Nuevo_stok)
            print("Stok actualizado exitosamente")
        else:
            print("producto no encontrado")

def Menu():
    Sistema = sistema_de_productos()
    while True:

        print("Sistema Gestion de productos")
        print("1: gregar un producto")
        print("2: Mostrar porductos")
        print("3: Buscar productos")
        print("4: Actualizar precio")
        print("5: Actualizar Stok ")
        print("6 vender producto ")
        print("7: Eliminar producto")
        print("8 SALIR")       

        Opcion = input("Ingrese una opciòn")
        if Opcion == "1":
            codigo = input("Ingrese el codigo del producto")
            nombre =  input("Ingrese el nombre del prodcuto")
            precio = float(input("Ingrse el precio del producto"))
            stok = int(input("Ingrese el Stok del producto"))
            Nuevo_producto = producto(codigo, nombre, precio, stok)
            Sistema.agregar_producto(Nuevo_producto)
            
        elif Opcion == "2":
            Sistema.mostrar_producto()
        elif Opcion == "3":
            codigo =input("INGRESE EL CODIGO DEL PRODUCTO")
            producto = Sistema.Buscar_producto(codigo)
            if producto:
                producto.mostrar_info()
            else:
                print("Producto no encontrado ")
            
        elif Opcion == "4":
            codigo = input("Ingrese el codigo del producto")
            Nuevo_precio = float(input("Ingrese el nuevo precio"))
            Sistema.actualizar_precio(codigo, Nuevo_precio)

        elif Opcion == "5":
            codigo = input("Ingrese el codigo del producto actualizado")
            Nuevo_stok = int(input("Ingrese el nuevo stok") )
            Sistema.actualizar_stok (codigo, Nuevo_stok)  
        
        elif Opcion == "6":
            Codigo = input("ingrese el codigo del prodcuto a vender ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            producto = Sistema.Buscar_producto(Codigo)
            if producto:
                if producto.vender(cantidad):
                    print("Producto vendido exitosamente")
        
        elif Opcion == "7":
            Codigo = input("Ingrese el codigo del prodcuto")
            Sistema.Eliminar_producto(Codigo)
        else:
            print("Opcion no Valida, Ingrese una opcion del 1 al 7")    
if __name__=="__main__": Menu()        
