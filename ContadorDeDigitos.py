num = int(input("Ingresa un número entero: "))
contador = 0
n = abs(num)  # Para evitar problemas con números negativos
while n > 0:
    n //= 10
    contador += 1

if contador == 0:  # Si el número era 0
    contador = 1

print(f"El número {num} tiene {contador} dígitos.")