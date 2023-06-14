import random

def mostrar_tablero(intentos):
    if intentos == 6:
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif intentos == 5:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif intentos == 4:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("=========")
    elif intentos == 3:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" \|   |")
        print("      |")
        print("      |")
        print("=========")
    elif intentos == 2:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" \|/  |")
        print("      |")
        print("      |")
        print("=========")
    elif intentos == 1:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" \|/  |")
        print("  |   |")
        print("      |")
        print("=========")
    else:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" \|/  |")
        print("  |   |")
        print(" /    |")
        print("=========")

def obtener_palabra_aleatoria():
    palabras = ["python", "programacion", "ahorcado", "computadora", "juego"]
    return random.choice(palabras)

def jugar_ahorcado():
    palabra = obtener_palabra_aleatoria()
    palabra_oculta = ["_" for _ in palabra]
    intentos = 6
    letras_adivinadas = []

    while True:
        mostrar_tablero(intentos)
        print("Palabra:", " ".join(palabra_oculta))
        print()

        if "_" not in palabra_oculta:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

        if intentos == 0:
            print("Oh no, has perdido. La palabra correcta era:", palabra)
            break

        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta nuevamente.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
        else:
            print("La letra no está en la palabra. Intenta nuevamente.")
            intentos -= 1

        print()

    jugar_nuevamente = input("¿Quieres jugar nuevamente? (s/n): ").lower()
    if jugar_nuevamente == "s":
        jugar_ahorcado()

jugar_ahorcado()
