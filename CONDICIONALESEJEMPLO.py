#Importar una libreria 
from decimal import Decimal, ROUND_HALF_UP
#MAYORIA DE EDAD 

edad = Decimal(input("ESCRIBE TU EDAD: "))
edad = edad.quantize(Decimal('0.0'),rounding=ROUND_HALF_UP)#round(edad,1) #FUNCION PARA REDONDEAR (PARAMETROS O ARGUMENTOS)
print(edad)

if( edad >= 18 and edad <= 120): #RANGO VALIDO DE 18 A 120
    print("ES MAYOR DE EDAD")
elif( edad >= 0 and edad < 18): #RANGO VALIDO 0 A 17 
    print("ES MENOR DE EDAD")
elif( edad < 0 or edad > 120): #VALORES MO VALIDOS MENOR QUE 0 O MAYOR QUE 120 
    print("EDAD NO VALIDA")
else:
    print("OTRA COSA")
