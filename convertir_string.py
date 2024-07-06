texto = input("Ingrese un texto: ")

# Operación 1: Retornar todo el texto en mayúsculas
texto_mayusculas = texto.upper()
print("Texto en mayúsculas:", texto_mayusculas)

# Operación 2: Retornar todo el texto en minúsculas
texto_minusculas = texto.lower()
print("Texto en minúsculas:", texto_minusculas)

# Operación 3: Retornar los dos primeros caracteres del texto
dos_primeros_caracteres = texto[:2]
print("Dos primeros caracteres:", dos_primeros_caracteres)

# Operación 4: Retornar los dos últimos caracteres del texto
dos_ultimos_caracteres = texto[-2:]
print("Dos últimos caracteres:", dos_ultimos_caracteres)

# Operación 5: Retornar la cantidad de veces que se repite el último caracter
ultimo_caracter = texto[-1]
repeticiones_ultimo_caracter = texto.count(ultimo_caracter)
print("Cantidad de repeticiones del último caracter:", repeticiones_ultimo_caracter)

# Operación 6: Retornar el texto invertido
texto_invertido = texto[::-1]
print("Texto invertido:", texto_invertido)
