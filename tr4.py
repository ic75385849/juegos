import random

opciones = ["piedra", "papel", "tijera"]
puntos_fabricio = 0
puntos_PC = 0
max_puntos = 3  

print ('¿Hola, como te llamas?')
nombre=input()

while puntos_fabricio < max_puntos and puntos_PC < max_puntos:
    PC = random.choice(opciones)
    fabricio = input("Escribe piedra, papel o tijera: ")
    
    if fabricio not in opciones:
        print("Opción inválida. Por favor, elige piedra, papel o tijera.")
        continue
    
    print(f"Opción de la PC: {PC}")
    print(f"Opción de fabricio: {fabricio}")

    if fabricio == PC:
        print("Es un empate")
    elif (fabricio == "piedra" and PC == "tijera") or (fabricio == "papel" and PC == "piedra") or (fabricio == "tijera" and PC == "papel"):
        print("Has ganado esta ronda")
        puntos_fabricio += 1
    else:
        print("Has perdido esta ronda")
        puntos_PC += 1
    
    print(f"Puntos de fabricio: {puntos_fabricio} - Puntos de la PC: {puntos_PC}")
    print()

if puntos_fabricio >= max_puntos:
    print("Has ganado el juego")
elif puntos_PC >= max_puntos:
    print("la PC ha ganado el juego")