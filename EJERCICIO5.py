# Obtener valores para: a, b y c. Calcular la fórmula general.

a = float(input("Dame el valor de a:"))
b = float(input("Dame el valor de b:"))
c = float(input("Dame el valor de c:"))

#Calculamos lo de adentro de la raíz o con otro nombre discriminante 

disc = pow((b**2) - (4*a*c),1/2)

#Calcular las dos soluciones

raíz_1 = ((-b + disc)/(2*a))
raíz_2 = ((-b - disc)/(2*a))

#MOSTRAR EN PANTALLA RESULTADOS

print("EL RESULTADO DE LA PRIMER RAÍZ ES:",raíz_1)
print("EL RESULTADO DE LA SEGUNDA RAÍZ ES:",raíz_2)