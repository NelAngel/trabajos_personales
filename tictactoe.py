def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-----")


def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True

    # Verificar columnas
    for columna in range(3):
        if all(tablero[fila][columna] == jugador for fila in range(3)):
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False


def jugar_tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        fila = int(input("Ingrese el número de fila (0, 1, 2): "))
        columna = int(input("Ingrese el número de columna (0, 1, 2): "))

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual

            if verificar_ganador(tablero, jugador_actual):
                print("¡Felicidades! El jugador", jugador_actual, "ha ganado.")
                break

            if jugador_actual == "X":
                jugador_actual = "O"
            else:
                jugador_actual = "X"
        else:
            print("Esa casilla ya está ocupada. Intenta nuevamente.")

        # Verificar si hay un empate
        if all(casilla != " " for fila in tablero for casilla in fila):
            print("El juego ha terminado. Es un empate.")
            break


jugar_tres_en_raya()
