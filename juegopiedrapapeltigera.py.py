import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    usuario = input("Elige piedra, papel o tijera: ").lower()
    
    if usuario not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        return
    
    computadora = random.choice(opciones)
    
    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")

    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

# Bucle para jugar varias veces
while True:
    jugar()
    otra = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if otra != 's':
        print("¡Gracias por jugar!")
        break