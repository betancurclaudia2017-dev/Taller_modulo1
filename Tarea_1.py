def registrar_estudiante():
    """
    permite ingresar un nuevo estudiante
    """
    list_datos= []
    nombre=input("Ingrese el nombre del estudiante: ")
    list_datos.append(nombre)
    edad=int(input("Ingrese la edad: "))
    edad_validada = limitante_edad(edad)
    list_datos.append(edad_validada)
    for i in range(0,3):
        nota=float(input(f"Ingrese la nota {i+1}: "))
        nota_validada=limitante_notas(nota)
        list_datos.append(nota_validada)
    return list_datos

def limitante_edad(edad_estudiante):
    """
    valida que la edad sea positiva
    """
    while edad_estudiante < 0:
        print("la edad debe ser un numero entero positivo. Vuelva a intentarlo.")
        edad_estudiante=int(input("Ingrese la edad: "))
    return edad_estudiante


def limitante_notas(note):
    """
    limita los valores que puede tomar una nota ingresada
    """
    while note > 5.0 or note < 0.0:
        print("Este parcero iske tin!")
        note= float(input("Ingrese una nota valida (entre 0 y 5): "))
    return  note

def calcular_promedio(n1,n2,n3):
    """
    calcula el promedio de un estudiante
    """
    promedio1 = (n1+n2+n3)/3
    return promedio1

def calcular_promedio_grupo(lista_estudiantes:list):
    """
    calcula el el promedio total del grupo de estudiantes ingresados
    """
    promedios_individuales = []
    suma_promedios = 0
    for estudiante in lista_estudiantes:
        nota1 = estudiante[2]
        nota2 = estudiante[3]
        nota3 = estudiante[4]
        promedios_individuales.append(calcular_promedio(nota1,nota2,nota3))
    for promedio in promedios_individuales:
        suma_promedios += promedio
    return suma_promedios/len(promedios_individuales)

def evaluar_estado(promedio):
    if promedio >= 4.0:
        return "Aprovado"
    elif promedio >= 3.0 and promedio <4.0:
        return "En recuperacion"
    else: 
        return "Reprobado"

def director_de_orquesta():
    """
    ordena la ejecucion de las demas funciones
    """
    lista_estudiantes=[]
    i = 0
    menu= """
===== SISTEMA DE ESTUDIANTES =====

        1. Registrar estudiante
        2. Salir
    """
    while True:
        print(menu)
        opcion= int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                datos_estudiante = registrar_estudiante()
                lista_estudiantes.append(datos_estudiante)
                print("-"*14)
                print(f"\nEstudiante {i+1}")
                print("-"*14)
                print(f"Nombre del estudiante: {lista_estudiantes[i][0]}")
                print(f"Edad del estudiante: {lista_estudiantes[i][1]}")
                print(f"Nota1 del estudiante: {lista_estudiantes[i][2]}")
                print(f"Nota2 del estudiante: {lista_estudiantes[i][3]}")
                print(f"Nota3 del estudiante: {lista_estudiantes[i][4]}")
                promedio_estudiante = calcular_promedio(lista_estudiantes[i][2],lista_estudiantes[i][3],lista_estudiantes[i][4])
                print("-"*14)
                print("Promedio del estudiante: ",promedio_estudiante) 
                print(f"Estado del estudiante: {evaluar_estado(promedio_estudiante)}")
                print("-"*14)
                i = i+1             
            case 2:
                promedio_grupo = calcular_promedio_grupo(lista_estudiantes)
                total_estudiantes_ingresados = len(lista_estudiantes)
                print("="*15)
                print("Promedio general del grupo: ",promedio_grupo)
                print("Total estudiantes ingresados: ", total_estudiantes_ingresados)
                break  


director_de_orquesta()