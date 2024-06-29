while True:
    a= int(input("jugador 1: 1=piedra, 2=papel, 3=tijera: "))
    b= int(input("jugador 2: 1=piedra, 2=papel, 3=tijera: "))

    if a == 1 and b == 3:
        print('jugador 1 gana: piedra gana a tijera')
    elif a == 2 and b == 1:
        print('jugador 1 gana : papel gana a piedra')
    elif a == 3 and b ==2:
        print('jugador 1 gama : tijera gana a papel')
    elif b == 1 and a== 3:
        print('jugador 2 gana: piedra gana a tijera')
    elif b == 2 and a == 1:
        print('jugador 2 gana: papel gana a piedra')
    elif b == 3 and a == 2: 
        print('jugador 2 gana: tijera gana a papel')
    else: 
        print('ninguno gana')