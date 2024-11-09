# Operaciones Matemáticas: Suma, Resta , Mult, Div, Potencia, Raíz cuadrada, Raíz cúbica, Módulo

# Declarar o crear las variables o constantes
núm_1 = 0  # valor inicial
núm_2 = 0  # valor inicial


# CONSTANTES



# Entradas
núm_1 = int(input("Ingresa un número:")) #input es un tipo de dato string y con el int estamos casteando para que se hagan enteros
núm_2 = int(input("Ingresa otro número:"))  # si quieres poner decimales puedes poner un float para que se impriman decimales

# Proceso(realizan las operaciones o cálculos matemáticos y/o lógicos)
suma = núm_1 + núm_2 #SUMA
resta = núm_1 - núm_2 #RESTA
mult = núm_1 * núm_2 #MULT




# Salidas (IMPRIMIR O MOSTRAR EN PANTALLA)
print("LA SUMA ES = " ,suma) # CONCATENACIÓN (unión) CON LA COMA (,)
print(' LA RESTA ES = ' + str(resta )) # CONCATENACIÓN (unión) con (+) POR CASTEO(Convertir un tipo de dato a otro tipo de dato)
print(f" LA MULTIPLICACIÓN ES = {mult}") #INTERPOLACIÓN DE TEXTO