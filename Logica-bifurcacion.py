palabra = input( "Introduce una palabra:")
longitud = len(palabra)

if longitud < 4 :
    print( "La palabra tiene menos de 4 letras")

elif longitud > 8 :
    print( "La palabra tiene más de 8 letras")

else :
    print( "La palabra tiene entre 4 y 8 letras")

x = float(input( "Introduce el valor de x:"))
y = float(input( "Introduce el valor de y:"))

if x > 0 and y > 0 :
    print( "El punto se encuentra en el cuadrante I")

elif x < 0 and y > 0 :
    print( "El punto se encuentra en el cuadrante II")

elif x < 0 and y < 0 :
    print( "El punto se encuentra en el cuadrante III")

elif x > 0 and y < 0 :
    print( "El punto se encuentra en el cuadrante IV")