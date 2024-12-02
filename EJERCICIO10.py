# 10. Obtener un número y determinar lo siguiente:
# a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
# b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
# c) en otro caso imprimir No Válido

def asignar_núm():
   núm = int(input("Ingrese un número: ")) 


   if(núm < 0 and núm > -100):
      print("MOSTRAR NÚMEROS IMPARES DE FORMA DESCENDENTE: ")
      for i in range(-1, núm - 1,-2):
       print(i) 
   elif(núm > 0 and núm < 100):    
      print("MOSTRAR LOS NÚMEROS PARES DE FORMA ASCENDENTE: ")
      for i in range(2, núm + 1,2):
        print(i)
   else:
      print("Opción no válida")

asignar_núm()     
     

