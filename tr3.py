import random

Moneda = ["Cara", "Cruz"]
print("¿Hola como te llamas?")
nombre = input()
print("¿Quieres Cara o Cruz?")
eleccion = input()
aleatorio = random.choice(Moneda)
print(aleatorio)
resultado = aleatorio
if resultado == "Cara":
    print("¡Has ganado!")
else:
    print("¡Has perdido!")