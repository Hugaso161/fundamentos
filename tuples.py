# Filtrar elementos
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Filtrar números impares
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]

# Operaciones matemáticas
numbers = [1, 2, 3, 4, 5]

# Sumar los elementos de una lista
sum_of_numbers = sum(numbers)
print(sum_of_numbers)  # Output: 15

# Acceder y modificar elementos
fruits = ["apple", "banana", "cherry"]

# Acceder a un elemento específico en una lista
print(fruits[0])  # Output: 'apple'

# Modificar el valor de un elemento en una lista
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']
