#PEDIR LA CANTIDAD DE GRADOS Y CONVERTIRLOS A °C, °F Y °K.

g = float(input("DAME LOS GRADOS CELSIUS:"))
F = float(input("DAME LOS GRADOS FAHRENHEIT:"))
K= float(input("DAME LOS GRADOS KELVIN:"))

#OPERACIONES
#Kelvin a Celsius
c_1 = K - 273.15

#Fahrenheit a Celsius
c_2 = (5*(F-32))/9

#Celsius a Kelvin
k_1 = g + 273.15

#Kelvin a Fahrenheit 
f_1 = ((9*(K-273.15))/5) + 32

#Fahrenheit a Kelvin 
k_2 = ((5*(F-32))/9) + 273.15

#Celsius a Fahrenheit
f_2 = ((9*g)/5) + 32

#RESULTADOS

print("LOS RESULTADOS DE LAS OPERACIONES SON:")


print("DE KELVIN A CELSIUS ES:",c_1)
print("DE FAHRENHEIT A CELSIUS ES:",c_2)
print("DE CELSIUS A KELVIN ES:",k_1)
print("DE FAHRENHEIT A KELVIN ES:",k_2)
print("DE KELVIN A FAHRENHEIT ES:",f_1)
print("DE CELSIUS A FAHRENHEIT ES:",f_2)


