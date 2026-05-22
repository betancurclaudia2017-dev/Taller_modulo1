estudiantes = {} #Creamos un diccionario vacio que va a recibir estudiantes
def agregar_estudiante(nombre): #Un metodo que nos va a permitir agregar nuevos estudiantes 
    if nombre in estudiantes:#Verificamos si el estudiante que vamos a agregar ya se encuentra registrado en el diccionario 
        print ("el estudiante ya existe") #Nos dira: "El estudiante ya existe"
    else: #Si no
        estudiantes[nombre] = [] #Aquì creamos una lista vacia que nos guarda el nombre del nuevo estudiante
        print(f"Estudiante '{nombre}' agregado")

def agregar_calificaciones(nombre, nota):#Creamos un nuevo metodo que me permite agregarle una nota a un estudiante
    if nombre in estudiantes: #Si el estudiante esta registrado en el diccionario de estudiantes
        estudiantes[nombre].append(nota)#Usa el metodo append para agregar un nota a la lista, correspondiente al estudiante
        print(f"Nota {nota} agregada a {nombre}")
    else:
        print("El estudiante no existe")

def calcular_promedio(nombre):
    if nombre in estudiantes:
        notas = estudiantes[nombre] #Obtiene la lista
        if len(notas) == 0:#Si la cantidad de notas del estudiante es igua a cero entonces retornara 0
            return 0 
        return sum(notas) / len(notas)#Sumaremos todas las notas divido por la catidad de notas y esto sacara elpromedio del estudiante
    else:
        print("El estudiante no existe")
        return None 

def mostrar_estudiante():
    if not estudiantes:
        print("No hay estudiantes registrados")
        return 
    for nombre in estudiantes:#Recorre cada estudiante
        promedio = calcular_promedio(nombre) 
        print(f"{nombre}: promedio = {promedio:.2f}") #Llama a la funcion promedio y el .2f muestra solo decimales

def mejor_estudiante():
    if not estudiantes:
        print("No hay studiantes registrados")
        return
    mejor = None 
    mejor_promedio = -1
    for nombre in estudiantes:
        promedio = calcular_promedio(nombre)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor = nombre 
    print (f" Mejor estudiante:{mejor} con promedio { mejor_promedio}")

def Eliminar_estudiante(nombre):
    if nombre in estudiantes:
        del estudiantes [nombre]
        print(f"Estudiante '{nombre}' Eliminado")
    else:
        print("El estudiante no existe")

agregar_estudiante("Ana")
agregar_estudiante("Luis")

agregar_calificaciones("Ana", 4.5)
agregar_calificaciones("Ana", 3.8)

mostrar_estudiante()
mejor_estudiante()


    



