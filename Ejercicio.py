#Cree una lista
a = ["Fresa", "Manzana", "Pera", "Naranja", "Sandia"]
#Cree una variable iniciada en cero
total = 0 
#El ciclo for, Para cada Fruta en la lista a
for Fruta in a:
    #Le aumente el valor que tiene en longitud de elemento
    total += len(Fruta)
print("Total de caracteres es:", total)

posicion = 0 
while posicion < len(a):
    print(a[posicion])
    posicion +=1



