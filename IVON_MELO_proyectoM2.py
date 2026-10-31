# =============================================
# PROYECTO FINAL - MÓDULO 2.
# Fundamentos de Python.
# =============================================

# Mantenemos el menú activo hasta seleccionar la opción de salida.
while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Validación de longitud")
    print("2. Identificación de cuadrantes")
    print("3. Salir")
    # Convertimos la opción del menú a entero y controlamos entradas no numéricas.
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: debe introducir una opción numérica.")
        continue
    # Validamos la cantidad de caracteres de la palabra ingresada.   
    if opcion == 1:
        palabra = input("Introduce una palabra: ")
        longitud = len(palabra)
        if longitud < 4:
            print("La palabra tiene menos de 4 letras")
        elif longitud > 8:
            print("La palabra tiene más de 8 letras")
        else:
            print("La palabra tiene entre 4 y 8 letras")
    # Solicitamos coordenadas y validamos que sean números distintos de cero.      
    elif opcion == 2:
        while True:
            try:
                x = float(input("Introduce el valor de x: "))
                if x != 0:
                    break
                print("Error: x no puede ser cero")
            except ValueError:
                print("Error: Introduce un valor numérico")
                    
        while True:
            try:
                y = float(input("Introduce el valor de y: "))
                if y != 0:
                    break
                print("Error: y no puede ser cero")
            except ValueError:
                print("Error: Introduce un valor numérico")
        print("Has seleccionado: Identificación de cuadrantes")   
        # Identificamos el cuadrante según el signo de las coordenadas.            
        if x > 0 and y > 0:
            print("Cuadrante I")
        elif x < 0 and y > 0:
            print("Cuadrante II")
        elif x < 0 and y < 0:
            print("Cuadrante III")
        elif x > 0 and y < 0:
            print("Cuadrante IV")
    # Finalizamos el programa cuando el usuario selecciona la opción de salida.        
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente")
