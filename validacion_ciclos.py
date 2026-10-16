palabra = input("Introduce una palabra:")
longitud = len(palabra)

while longitud < 4 or longitud > 8 :
    print("Error: la palabra debe tener entre 4 y 8 letras")
    palabra = input("Introduce una palabra:")
    longitud = len(palabra)

print("Palabra válida:", palabra)



x = float(input("Introduce el valor de x:"))

while x == 0 :
    print("Error: x no puede ser cero")
    x = float(input("Introduce el valor de x:"))

y = float(input("Introduce el valor de y:"))

while y == 0 :
    print("Error: y no puede ser cero")
    y = float(input("Introduce el valor de y:"))

if x > 0 and y > 0 : 
    print("El punto se encuentra en el cuadrante I")

elif x < 0 and y > 0 :
    print("El punto se encuentra en el cuadrante II")

elif x < 0 and y < 0 :
    print("El punto se encuentra en el cuadrante III")

elif x > 0 and y < 0 :
    print("El punto se encuentra en el cuadrante IV")