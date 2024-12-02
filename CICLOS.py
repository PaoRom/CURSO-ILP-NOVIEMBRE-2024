#CICLO FOR (PARA)
#SINTAXIS
'''
 for variable in range (valor_inicial,valor final, incremento/decremento):
  proceso del ciclo
'''
#EJEMPLO
'''
for i in range(100, -1, -1): # (VALOR INICIAL, CONDICIÓN FINAL: i < 10, incremento)
 print(i)
'''
'''
PRUEBA DE ESCRITORIO 
                    variable i       proceso imprimir i
 valor inicial          1            1 
 valor actual           2            2
 valor actual           3            3
                        4            4 
 valor final            9            9
 valor final            10           

'''


#CICLO WHILE (Mientras)
#SINTAXIS
'''
valor inicial
whiles (condición):
  proceso del ciclo
  incremento/decremento

'''

#EJEMPLO
#CICLO DEFINIDO
i = 1            #Valor inicial
while(i <= 1000):  #Condición
  print(i)       #proceso
  i = i + 1      #i +- incremento / decremento


#CICLO INDEFINIDO  
respuesta = "si"
while(respuesta == "si"):
 print("HOLA")
 respuesta = input("¿Quieres seguir?: ")

#CICLO INFINITO
i = 1
while(i > 0):
 print(i)
 i = i + 1 


