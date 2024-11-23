# Pedir el nivel del agua en metros de una cisterna

niv_agua = float(input("INGRESE EL NIVEL DE AGUA EN METROS: "))

#EVENTO
if(niv_agua > 6):
  print("DESBORDAMIENTO DE AGUA")
elif(niv_agua == 6):
  print("APAGANDO BOMBA")
elif(niv_agua >= 4 and niv_agua < 6):
  print("DESACELERAR BOMBA")  
elif(niv_agua >= 2 and niv_agua < 4):
  print("BOMBA TRABAJANDO")  
elif(niv_agua > 0 and niv_agua < 2): 
  print("ACELERAR BOMBA")
elif(niv_agua == 0):
  print("ENCENDIENDO BOMBA")
elif(niv_agua < 0):
  print("FUGA EN CISTERNA")



