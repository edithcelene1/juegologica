# juegologica
Juego de piedra papel o tigera spyder(pyton)
Las librerias que se utilizaron _ import ramdon
Mensajes intercalados y pausa 
Este es un juego sencillo que se uso en contra la computadora 

¿Como se juega?
1. Ingresa tu elección: `piedra`, `papel` o `tijera`.
2. El programa mostrará la elección de la computadora y determinará el ganador.
3. Después de cada ronda, puedes decidir si deseas jugar otra vez.
   
 Reglas del juego
 
- **Piedra** vence a **Tijera**
- **Tijera** vence a **Papel**
- **Papel** vence a **Piedra**
- Si ambos eligen lo mismo, es un **empate**
  
    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
  SI DESEAS SALIR (S/N)
  N = SALIR 
