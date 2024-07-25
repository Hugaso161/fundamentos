# Función de Saludo
def saludo(nombre):
    return f"Hola, {nombre}!"

# Función de Suma
def suma(a, b):
    return a + b

# Área de un Rectángulo
def area_rectangulo(largo, ancho):
    return largo * ancho

# Número Par o Impar
def es_par_o_impar(numero):
    return "Par" if numero % 2 == 0 else "Impar"

# Conversión de Grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Máximo de Tres Números
def maximo_de_tres(a, b, c):
    return max(a, b, c)

# Palíndromo
def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Contar Vocales
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for char in cadena if char in vocales)

# Números Primos
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Llamadas a las funciones con ejemplos
print(saludo("Juan"))
print(suma(3, 5))
print(area_rectangulo(4, 6))
print(es_par_o_impar(7))
print(celsius_a_fahrenheit(25))
print(maximo_de_tres(3, 7, 5))
print(es_palindromo("Anita lava la tina"))
print(factorial(5))
print(contar_vocales("Hola Mundo"))
print(es_primo(11))
