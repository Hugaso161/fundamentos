tipo_peso = input("Desea ingresar su peso en Kg o Lbs: ")
if tipo_peso.strip().lower() == "kg":
  peso = input("Ingrese su peso en kg: ")
else:
  peso = input("Ingrese su peso en lb: ")
  peso = float(peso)/2.2

altura = input("Ingrese su altura en metros: ")

imc = float(peso) / float(altura) ** 2
if imc <18.5:
  print(f"Su IMC es {imc}, usted tiene un Bajo peso")
elif imc >=18.5 and imc <25:
  print(f"Su IMC es {imc}, usted tiene un Peso normal")
elif imc >=25 and imc <30:
  print(f"Su IMC es {imc}, usted tiene Sobrepeso")
elif imc >=30 :
 print(f"Su IMC es {imc}, usted tiene obesidad")
