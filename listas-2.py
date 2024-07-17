# 1. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído.
numeros = []
for i in range(10):
    numero = int(input("Ingrese un entero: "))
    numeros.append(numero)
numero_max = max(numeros)
posicion_max = numeros.index(numero_max)
print(f"La posición del número mayor es: {posicion_max}")

# 2. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número par leído.
numeros_pares = [numero for numero in numeros si numero % 2 == 0]
numero_par_max = max(numeros_pares)
posicion_par_max = numeros.index(numero_par_max)
print(f"La posición del mayor número par es: {posicion_par_max}")

# 3. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros_primos = [numero for numero in numeros si es_primo(numero)]
numero_primo_max = max(numeros_primos)
posicion_primo_max = numeros.index(numero_primo_max)
print(f"La posición del mayor número primo es: {posicion_primo_max}")

# 4. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo
def empieza_con_digito_primo(n):
    primer_digito = int(str(n)[0])
    return es_primo(primer_digito)

contador = sum(1 para numero en numeros si empieza_con_digito_primo(numero))
print(f"La cantidad de números que comienzan con un dígito primo es: {contador}")

# 5. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.
def contar_digitos_pares(n):
    return sum(1 para digito en str(n) si int(digito) % 2 == 0)

numeros_primos = [numero para numero en numeros si es_primo(numero)]
numero_primo_max = max(numeros_primos, key=contar_digitos_pares)
posicion_primo_max = numeros.index(numero_primo_max)
print(f"La posición del número primo con más dígitos pares es: {posicion_primo_max}")

# 6. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos
posiciones = [i para i, numero en enumerate(numeros) si len(str(numero)) > 3]
print(f"Las posiciones de los números con más de 3 dígitos son: {posiciones}")

# 7. Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista
promedio = sum(numeros) // len(numeros)
print(f"El promedio entero de los números es: {promedio}")

# 8. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.
contador_negativos = sum(1 para numero en numeros si numero < 0)
print(f"La cantidad de números negativos es: {contador_negativos}")

# 9. Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenándolos en otra lista
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factoriales = [factorial(numero) para numero en numeros]
print(f"Los factoriales de los números son: {factoriales}")

# 10. Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.
dividendo = int(input("Ingrese un entero: "))
divisores = sum(1 para numero en numeros si dividendo % numero == 0)
print(f"La cantidad de divisores exactos de {dividendo} en la lista es: {divisores}")
