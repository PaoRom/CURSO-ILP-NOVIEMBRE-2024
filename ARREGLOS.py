#ARREGLOS (ARRAYS)/LISTAS
#Colección de elementos o valores de uno o más tipos de datos 
#SINTAXIS para declarar o crear un arreglo
'''
 nombre_Del_Arreglo = [elemento/valores]
''' 

#ENTRADA DE DATOS
nombres     =       ["Christopher",'Pablo',"Eduardo",'Carlos',"Paola"]
#INDICES (INDEX)          0           1         2        3        4    
edades     =      [ 20, 30, 45, 12, 18]
#INDICES (INDEX)    0    1   2   3   4
arreglo_lista = [10, 5.7, "Hola", True]
#INDICES (INDEX)  1   2      3      4 

#PROCESO: OPERACIONES CON ARREGLOS 
'''Modificación de un elemento del Arreglo '''
nombres[0] = "Christopher Chong Salazar"
edades[1] = 50
arreglo_lista[3] = False

''' Agregar un elemento del Arreglo '''
nombres.append("Andrea")
edades.append(15)
arreglo_lista.append("ILP")

''' Ordenar los elementos del Arreglo de forma alfabética o ascendente '''
nombres.sort()
edades.sort()

''' Limpia o vacía los elementos de la lista o arreglo '''
nombres.clear()

# SALIDA DE DATOS
print(nombres)
print(edades)
print(arreglo_lista)