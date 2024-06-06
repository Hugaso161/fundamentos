def suma(num):
  sum = 0
  while num > 0:
      sum += num % 10
      num //= 10
  return sum

def es_primo(num):
  if num < 2:
      return False
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          return False
  return True


num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

diff = abs(num1 - num2)
if diff % 10 == 4:
  digitos = [int(digito) for digito in str(num1)] + [int(digito) for digito in str(num2)]
  print("Digitos:", digitos)
elif  diff % 2 == 0:
  suma_digitos = suma(num1) + suma(num2)
  print("Suma de dígitos:", suma_digitos)
elif es_primo(diff) and diff < 10:
  producto = num1 * num2
  print("Producto de números:", producto)

else:
  print("Ninguna condición coincidente.")
