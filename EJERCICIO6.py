# Pedir un número y decir si es par o impar.

núm = int(input("Ingresa cualquier número: "))

if(núm % 2 == 0): # % SE UTILIZA PARA SABER SI UN NUMERO ES DIVISIBLE DE MANERA UNIFORME POR OTRO
    print("EL NUMERO ES PAR")
elif(núm % 2 == 1): # DEPENDE A LO QUE TE RETORNE ES LO QUE DARA 
    print("EL NUMERO ES IMPAR")    