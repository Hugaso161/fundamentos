# 1. Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído.
def mostrar_enteros(num):
    for i in range(1, num + 1):
        print(i)


# 2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.
def mostrar_pares(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)


# 3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído.
def mostrar_divisores(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


# 4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.
def mostrar_enteros_entre(num1, num2):
    for i in range(num1, num2 + 1):
        print(i)


# 5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.
def mostrar_terminados_en_4(num1, num2):
    for i in range(num1, num2 + 1):
        if i % 10 == 4:
            print(i)


# 6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.
def mostrar_enteros_por_digitos(num):
    for digit in str(num):
        digit = int(digit)
        for i in range(1, digit + 1):
            print(i)


# 7. Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.
def mostrar_enteros_1_al_100():
    for i in range(1, 101):
        print(i)


# 8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200.
def mostrar_pares_20_al_200():
    for i in range(20, 201):
        if i % 2 == 0:
            print(i)


# 9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.
def mostrar_terminados_en_6_25_al_205():
    for i in range(25, 206):
        if i % 10 == 6:
            print(i)


# 10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.
def suma_enteros(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print("La suma de los enteros comprendidos entre 1 y", num, "es:", sum)


# 11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.
def mostrar_enteros_entre_digitos(num):
    digit1 = num // 10
    digit2 = num % 10
    for i in range(digit1, digit2):
        print(i)


# 12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.
def tiene_digito_1(num):
    has_digit_1 = False
    for digit in str(num):
        if digit == '1':
            has_digit_1 = True
            break
    if has_digit_1:
        print("El número", num, "tiene el dígito 1.")
    else:
        print("El número", num, "no tiene el dígito 1.")


# 13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.
def mostrar_multiplos_de_5(num):
    for i in range(1, num + 1):
        if i % 5 == 0:
            print(i)


# 14. Mostrar en pantalla los primeros 20 múltiplos de 3.
def mostrar_primeros_multiplos_de_3():
    count = 0
    for i in range(1, 100):
        if i % 3 == 0:
            print(i)
            count += 1
            if count == 20:
                break


# 15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.
def suma_primeros_multiplos_de_3():
    sum = 0
    count = 0
    for i in range(1, 100):
        if i % 3 == 0:
            sum += i
            count += 1
            if count == 20:
                break
    print("La suma de los primeros 20 múltiplos de 3 es:", sum)


# 16. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.
def comparar_promedios_multiplos(x, y):
    sum_multiples_of_2 = 0
    sum_multiples_of_5 = 0
    count_multiples_of_2 = 0
    count_multiples_of_5 = 0
    for i in range(1, 100):
        if i % 2 == 0:
            sum_multiples_of_2 += i
            count_multiples_of_2 += 1
            if count_multiples_of_2 == x:
                break
        if i % 5 == 0:
            sum_multiples_of_5 += i
            count_multiples_of_5 += 1
            if count_multiples_of_5 == y:
                break
    average_multiples_of_2 = sum_multiples_of_2 / x
    average_multiples_of_5 = sum_multiples_of_5 / y
    if average_multiples_of_2 > average_multiples_of_5:
        print("El promedio de los", x,
              "primeros múltiplos de 2 es mayor que el promedio de los", y,
              "primeros múltiplos de 5.")
    else:
        print("El promedio de los", x,
              "primeros múltiplos de 2 no es mayor que el promedio de los", y,
              "primeros múltiplos de 5.")


# 17. Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5.
def promedio_terminados_en_5():
    count = 0
    sum_ending_in_5 = 0
    while True:
        num = int(input("Ingrese un número (0 para terminar): "))
        if num == 0:
            break
        if num % 10 == 5:
            sum_ending_in_5 += num
            count += 1
    average_ending_in_5 = sum_ending_in_5 / count
    print("El promedio de los números terminados en 5 es:",
          average_ending_in_5)


# 18. Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1.
def generar_numeros_del_1_al_10():
    for i in range(10, 0, -1):
        print(i)


# 19. Leer un número entero y mostrar en pantalla su tabla de multiplicar.
def tabla_de_multiplicar(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


# 20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.
def sumatoria_de_factoriales(num):
    factorial_sum = 0
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
        factorial_sum += factorial
    print(
        "La sumatoria de las factoriales de los números comprendidos entre 1 y",
        num, "es:", factorial_sum)
# mostrar_enteros(10)
# mostrar_pares(10)
# mostrar_divisores(10)
# mostrar_enteros_entre(5, 10)
# mostrar_terminados_en_4(1, 14)
# mostrar_enteros_por_digitos(123)
# mostrar_enteros_1_al_100()
# mostrar_pares_20_al_200()
# mostrar_terminados_en_6_25_al_205()
# suma_enteros(10s
# mostrar_enteros_entre_digitos(26)
# tiene_digito_1(123)
# mostrar_multiplos_de_5(10)
# mostrar_primeros_multiplos_de_3()
# suma_primeros_multiplos_de_3()
# comparar_promedios_multiplos(5, 3)
# promedio_terminados_en_5()
# generar_numeros_del_1_al_10()
# tabla_de_multiplicar(12)
# sumatoria_de_factoriales(5)
