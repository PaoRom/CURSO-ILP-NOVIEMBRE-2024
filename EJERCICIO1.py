# Calcular el promedio de 3 calificaciones

#VARIABLES
cal_1 = float(input("Introduce la primer calificación:"))
cal_2 = float(input("Introduce la segunda calificación:"))
cal_3 = float(input("Introduce la tercer calificación:"))

# PROMEDIO

promedio = (cal_1 + cal_2 + cal_3)/3

# RESULTADO

print("EL PROMEDIO DE LAS CALIFICACIONES ES:" ,promedio)

#VERIFICAR SI EL PROMEDIO ES APROBATORIO O REPROBATORIO 
if(promedio > 6 and promedio <= 10):
     print("APROBO EL CURSO FELICIDADES ")
elif(promedio == 6):
     print("UY PANSASTE")     
elif(promedio < 6 and promedio >= 0):
     print("REPROBASTE SIGUE PARTICIPANDO")
elif(promedio < 0 or promedio > 10):
     print("ESO NI EXISTE")    
    