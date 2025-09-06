num = int(input("Ingresa un número entero: "))

invertido = 0
n = abs(num)

while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n //= 10

if num < 0:
    invertido *= -1  # conservar el signo

print(f"El número invertido es: {invertido}")