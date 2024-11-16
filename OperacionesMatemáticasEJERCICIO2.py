# Operaciones Matemáticas: Suma, Resta , Mult, Div, Potencia, Raíz cuadrada, Raíz cúbica, Módulo

# IMPORTAR LAS LIBRERIAS O BIBLIOTECAS QUE CONTIENEN FUNCIONES
import math

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
potencia_1 = núm_1 ** núm_2 #Potencia
potencia_2 = pow(núm_1,núm_2) #Las funciones tienen paréntesis donde se colocan Parámetros o Argumentos
cuadrado = núm_1 ** 2
cubo = pow(núm_2,3)

raíz_cuadrada_1 = math.sqrt(16)
raíz_cuadrada_2 = pow(16,1/2)
raíz_cúbica = pow(27,1/3)

módulo_residuo_1 = 10 % 2
módulo_residuo_2 = núm_1 % núm_2

# Salidas (IMPRIMIR O MOSTRAR EN PANTALLA)
print("LA SUMA ES = " ,suma) # CONCATENACIÓN (unión) CON LA COMA (,)
print(' LA RESTA ES = ' + str(resta )) # CONCATENACIÓN (unión) con (+) POR CASTEO(Convertir un tipo de dato a otro tipo de dato)
print(f" LA MULTIPLICACIÓN ES = {mult}") #INTERPOLACIÓN DE TEXTO
print("LA POTENCIA DE n1 ELEVADO A n2 =",potencia_1)
print("LA POTENCIA DE n1 ELEVADO A n2 =",potencia_2)
print("EL CUADRADO DE n1 = ",cuadrado)
print("EL CUADRADO DE n1 = ",cubo)
print("EL CUBO DE n2 =",cubo)
print("LA RAÍZ CUADRADA DE 16 ES=",raíz_cuadrada_1)
print("LA RAÍZ CUADRADA DE 16 ES=",raíz_cuadrada_2)
print("LA RAÍZ CÚBICA DE 27 ES=",raíz_cúbica)
print("MÓDULO 1 O RESIDUO ES=",módulo_residuo_1)
print("MÓDULO 2 O RESIDUO ES=",módulo_residuo_2)
