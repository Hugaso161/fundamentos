def calcular_promedio(notasy):
  total = sum(notasy)
  promedio = total / len(notasy)
  return promedio

def calificacion_valida(calificacion):
  try:
      calificacion = float(calificacion)
      if calificacion < 0 or calificacion > 100:
          return False
      return True
  except ValueError:
      return False

def capturar_datos_estudiante():
  nombre = input("Ingrese el nombre del estudiante: ")
  id_estudiante = input("Ingrese el ID del estudiante: ")
  calificaciones = []
  for i in range(4):
      while True:
          calificacion = input(f"Ingrese la calificación {i+1}: ")
          if calificacion_valida(calificacion):
              calificaciones.append(float(calificacion))
              break
          else:
              print("Calificación no válida. Por favor, ingrese un número válido entre 0 y 100.")
  return nombre, id_estudiante, calificaciones

def imprimir_promedios_estudiantes(estudiantes):
  for estudiante in estudiantes:
      nombre, id_estudiante, calificaciones = estudiante
      promedio = calcular_promedio(calificaciones)
      print(f"Estudiante: {nombre} (ID: {id_estudiante}) - Promedio: {promedio}")

estudiantes = []
while True:
  nombre, id_estudiante, calificaciones = capturar_datos_estudiante()
  estudiantes.append((nombre, id_estudiante, calificaciones))
  eleccion = input("¿Desea capturar otro estudiante? (sí/no): ")
  if eleccion.lower().strip() != "si":
      break

imprimir_promedios_estudiantes(estudiantes)
