# Diccionario principal
estudiantes = {} #Aqui creamos un diccionario vacio

# 1. Agregar un nuevo estudiante
def agregar_estudiante(nombre):
    if nombre in estudiantes:
        print("El estudiante ya existe.")
    else:
        estudiantes[nombre] = []
        print(f"Estudiante '{nombre}' agregado.")

# 2. Agregar calificaciones
def agregar_calificacion(nombre, nota):
    if nombre in estudiantes:
        estudiantes[nombre].append(nota)
        print(f"Nota {nota} agregada a {nombre}.")
    else:
        print("El estudiante no existe.")

# 3. Calcular promedio de un estudiante
def calcular_promedio(nombre):
    if nombre in estudiantes:
        notas = estudiantes[nombre]
        if len(notas) == 0:
            return 0
        return sum(notas) / len(notas)
    else:
        print("El estudiante no existe.")
        return None

# 4. Mostrar todos los estudiantes con sus promedios
def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    for nombre in estudiantes:
        promedio = calcular_promedio(nombre)
        print(f"{nombre}: Promedio = {promedio:.2f}")

# 5. Encontrar el estudiante con mejor promedio
def mejor_estudiante():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    mejor = None
    mejor_promedio = -1
    
    for nombre in estudiantes:
        promedio = calcular_promedio(nombre)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor = nombre
    
    print(f"Mejor estudiante: {mejor} con promedio {mejor_promedio:.2f}")

# 6. Eliminar un estudiante
def eliminar_estudiante(nombre):
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante '{nombre}' eliminado.")
    else:
        print("El estudiante no existe.")


# --- Ejemplo de uso ---
agregar_estudiante("Ana")
agregar_estudiante("Luis")

agregar_calificacion("Ana", 4.5)
agregar_calificacion("Ana", 3.8)
agregar_calificacion("Luis", 4.9)
agregar_calificacion("Luis", 4.7)

mostrar_estudiantes()
mejor_estudiante()

eliminar_estudiante("Ana")
mostrar_estudiantes()