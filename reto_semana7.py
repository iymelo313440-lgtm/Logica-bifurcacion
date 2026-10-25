# Creamos una lista vacía para almacenar todos los intentos de palabras
# que el usuario introduzca durante la ejecución del programa.
palabras = []   # list: lista modificable de cadenas de texto (str).

# Solicitamos una palabra y la guardamos en la lista.
# Después validamos su longitud y registramos cada nuevo intento.
palabra = input("Introduce una palabra: ")
palabras.append(palabra)

longitud = len(palabra)   # int: cantidad de caracteres.

while longitud < 4 or longitud > 8:
    print("Error: la palabra debe tener entre 4 y 8 caracteres")
    palabra = input("Introduce una palabra: ")
    palabras.append(palabra)
    longitud = len(palabra)

print("Palabra válida:", palabra)

# Creamos una tupla con los nombres de los cuatro cuadrantes.
# Utilizamos sus índices para mostrar el cuadrante correspondiente.
cuadrantes = (  # tuple: colección inmutable de cadenas (str).
    "Cuadrante I",
    "Cuadrante II",
    "Cuadrante III",
    "Cuadrante IV"
)
print(cuadrantes)

# Solicitamos las coordenadas x e y.
# Los ciclos while impiden continuar mientras alguna coordenada sea cero.
# Convertimos las entradas de x e y al tipo float.
x = float(input("Introduce el valor de x: "))

while x == 0:
    print("Error: x no puede ser cero")
    x = float(input("Introduce el valor de x: "))

y = float(input("Introduce el valor de y: "))

while y == 0:
    print("Error: y no puede ser cero")
    y = float(input("Introduce el valor de y: "))

# Comparamos los signos de x e y para determinar el cuadrante.
# Cada índice de la tupla corresponde a uno de los cuatro cuadrantes.
if x > 0 and y > 0:
    print(cuadrantes[0])

elif x < 0 and y > 0:
    print(cuadrantes[1])

elif x < 0 and y < 0:
    print(cuadrantes[2])

elif x > 0 and y < 0:
    print(cuadrantes[3])

print("Palabras ingresadas:", palabras)
