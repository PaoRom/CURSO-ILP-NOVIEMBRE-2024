#Crear una lista o arreglo de diccionarios de 5 estados de México con los datos de nombre, población, extensión.

estados_mexico = [
    {"nombre": "CDMX", "población": 9209944, "extensión": 1485},
    {"nombre": "Jalisco", "población": 8348155, "extensión": 80330},
    {"nombre": "Nuevo León", "población": 5511100, "extensión": 64138},
    {"nombre": "Chihuahua", "población": 3800487, "extensión": 247087},
    {"nombre": "Yucatán", "población": 2333138, "extensión": 39600}
]

# Imprimir la lista de estados
for estado in estados_mexico:
    print(f"Estado: {estado['nombre']}, Población: {estado['población']}, Extensión: {estado['extensión']} km²")