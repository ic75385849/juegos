import random
def lanzar_moneda():
    return random.randint(1, 3)
def cara_o_sello():
    puntos_fabricio = 0
    puntos_maquina= 0

    print ('¿Hola, como te llamas?')
    nombre=input()

    while puntos_fabricio<5 and puntos_maquina<5:
        print(f"puntos: fabricio {puntos_fabricio}- pc {puntos_maquina}")
        elige_usuario= input("elige cara (1) o sello (2): ")
        elige_usuario=int(elige_usuario)

        if elige_usuario != 1 and elige_usuario != 2: 
            print("seleccion invalida deve elegir 1 o 2")
            continue
        resultado= lanzar_moneda()

        if resultado == 1:
            print("cara")

        else:
            print("sello")

        if elige_usuario== resultado:
            puntos_fabricio += 1
            print("punto para fabricio")
        else:
            puntos_maquina += 1
            print("para la otra sera. punto para la PC")
    if puntos_fabricio== 5:
        print("felicitaciones ganastes")
    else:
        print("para la otra sera la PC te gano")

cara_o_sello()
