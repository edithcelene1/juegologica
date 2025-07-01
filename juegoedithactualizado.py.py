import random

# Estadísticas para jugador contra computadora
estadisticas = {
    "jugadas": 0,
    "ganadas": 0,
    "perdidas": 0,
    "empates": 0}

def jugar_contra_computadora():
    opciones = ["piedra", "papel", "tijera"]
    usuario = input("Elige piedra, papel o tijera: ").lower()
    
    if usuario not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        return
    
    computadora = random.choice(opciones)
    
    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")

    estadisticas["jugadas"] += 1

    if usuario == computadora:
        print("¡Empate!")
        estadisticas["empates"] += 1
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
        estadisticas["ganadas"] += 1
    else:
        print("¡Perdiste!")
        estadisticas["perdidas"] += 1

def jugar_multijugador():
    opciones = ["piedra", "papel", "tijera"]
    
    jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
    if jugador1 not in opciones:
        print("Opción inválida para Jugador 1.")
        return

    print("\n" * 30)  # Simula limpieza de pantalla
    jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()
    if jugador2 not in opciones:
        print("Opción inválida para Jugador 2.")
        return

    print(f"Jugador 1 eligió: {jugador1}")
    print(f"Jugador 2 eligió: {jugador2}")

    if jugador1 == jugador2:
        print("¡Empate!")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        print("¡Jugador 1 gana!")
    else:
        print("¡Jugador 2 gana!")

def ver_estadisticas():
    print("\n--- ESTADÍSTICAS ---")
    print(f"Partidas jugadas: {estadisticas['jugadas']}")
    print(f"Ganadas: {estadisticas['ganadas']}")
    print(f"Perdidas: {estadisticas['perdidas']}")
    print(f"Empates: {estadisticas['empates']}")
    print("---------------------\n")

def menu():
    while True:
        print("====== MENÚ DEL JUEGO ======")
        print("1. Jugar contra la computadora")
        print("2. Jugar multijugador")
        print("3. Ver estadísticas")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            jugar_contra_computadora()
        elif opcion == "2":
            jugar_multijugador()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Iniciar el programa
menu()


