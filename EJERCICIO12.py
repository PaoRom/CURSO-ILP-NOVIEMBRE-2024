# Hacer una función para que imprima un arreglo o lista de 10 elementos numéricos insertados uno por uno y ordenados de forma ascendente y mostrarlos en pantalla.

def ingresar_y_ordenar():
    # Pedir los 10 números 
    lista_numeros = [
        float(input("Ingrese el primer número: ")),
        float(input("Ingrese el segundo número: ")),
        float(input("Ingrese el tercer número: ")),
        float(input("Ingrese el cuarto número: ")),
        float(input("Ingrese el quinto número: ")),
        float(input("Ingrese el sexto número: ")),
        float(input("Ingrese el séptimo número: ")),
        float(input("Ingrese el octavo número: ")),
        float(input("Ingrese el noveno número: ")),
        float(input("Ingrese el décimo número: "))
    ]

    # Ordenar la lista
    lista_numeros.sort()

    # Mostrar la lista ordenada
    print("\nLos números ordenados son:", lista_numeros)

# Llamar a la función
ingresar_y_ordenar()