#EJERCICIO 9
import random
import string
import os

def Mostrar_Menú():
    print("******** MENÚ ********")
    print("a) Mostrar una lista de 3 medios de transporte con sus estrellas de calificación")
    print("b) Calcular la nómina de un empleado en ENERO del 2024")
    print("c) Generar una contraseña con el número de caracteres pedidos menor o igual a 5, si es mayor que 5 mostrar mensaje de error")
    print("d) Pedir al usuario su nombre, primer ap., segundo ap. y edad e imprimir un saludo con sus datos")

def Lista_MedTransporte():
   lista_pasajes = ["Metro", "Avión", "Metrobús"]
   lista_estrellas_cal = [3, 4, 5]
   print(lista_pasajes, lista_estrellas_cal)

def Calcular_Nómina():
    pag_x_día = 250
    días_laborados = int(input("CUANTOS DÍAS USTED LABORO: "))
    total_de_nomina = (pag_x_día * días_laborados)
    print("SU NOMINA ES: $",total_de_nomina)

def Generar_Contraseña(número_caracteres):
 if(número_caracteres <= 5):
   #DEFINIR LOS CARACTERES A UTILIZAR
    caracteres = string.ascii_letters + string.digits + string.punctuation
   #GENERAR LA CONTRASEÑA ALEATORIA
    contraseña = ''.join(random.choice(caracteres)for _ in range(número_caracteres))
    return contraseña  
 elif(número_caracteres > 5):
     return "ERROR"
 
def NombreCompleto_y_edad():
 # Pedir al usuario su nombre, primer apellido, segundo apellido y edad
 nombre = input("¿Cuál es tu nombre? ")
 primer_apellido = input("¿Cuál es tu primer apellido? ")
 segundo_apellido = input("¿Cuál es tu segundo apellido? ")
 edad = input("¿Cuántos años tienes? ")
 print(f"Hola, {nombre} {primer_apellido} {segundo_apellido}! Tienes {edad} años.")
 

respuesta = "si"


while (respuesta == "si" or respuesta == "SI" or respuesta == "Y" or respuesta == "S"):
 os.system('cls')
 Mostrar_Menú() #Invocar o mandar a llamar la función
 opción = input("ELIGE UNA OPCIÓN DEL MENÚ: ")

 if(opción == "a" or opción == 'A' or opción == 'A)'):
    #CONTENIDO
    Lista_MedTransporte()    
 elif(opción == "b" or opción == 'B' or opción == 'B)'):
    Calcular_Nómina()    
 elif(opción == "c" or opción == 'C' or opción == 'C)'):
    caracteres = int(input ("¿Cuántos caracteres?: "))
    print(Generar_Contraseña(caracteres))
 elif(opción == "d" or opción == 'D' or opción == 'D)'):
      #IMPRIMIR SALUDO
      NombreCompleto_y_edad()
 else:     
    print("Opción no válida")

 respuesta = input("¿Quieres continuar?: ")