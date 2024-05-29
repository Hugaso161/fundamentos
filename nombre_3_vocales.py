vocales = ["a","e","i","o","u"]
nombre = input("Escribe el nombre: \n")
numero_vocales = 0

for item in list(nombre):
  if item in vocales:
    numero_vocales += 1

if numero_vocales >= 3:
  print("\n"+nombre+" tiene "+ str(numero_vocales)+" vocales")
else:
  print("No tiene 3 vocales")

