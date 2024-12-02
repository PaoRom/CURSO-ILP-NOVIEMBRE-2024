#Pedir números enteros en un ciclo mientras sean positivos y en caso de
#que un número sea negativo cerrar el ciclo y al final promediar los
#números positivos ingresados por el usuario.

def núm_promedio():
    suma = 0
    contador = 0
    numero = 0
    
    while(numero >= 0):  # Solo ejecutamos el ciclo si el número es positivo o 0
        numero = int(input("Ingrese un número entero: "))
        
        if numero >= 0:
            suma += numero
            contador += 1
    
    if contador > 0:
        print("El promedio es:", suma / contador)
    else:
        print("No se ingresaron números positivos.")

núm_promedio()