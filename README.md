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


  JUEGO ACTUALIZADO
  PIEDRA PAPEL Y TIGERA
  Este es un juego muy basico que se desarrollo en payton este juego deciende dos maneras al jugar tambien se lleva un registro de estadisticas para contabilizar la partida ganadas, pertidas y empatadas.
  * Contra la computadora(individualmente)
  * Multijugador (De dos usuarios)
  Reglas del juego
  Piedra gana a Tijera
  Tijera gana a Papel
  Papel gana a Piedra
  Extructura del codigo
  Si ambos jugadores eligen lo mismo, hay un empate
  jugar_contra_computadora(): Modo individual y actualización de estadísticas
  jugar_multijugador(): Permite dos jugadores humanos
  ver_estadisticas(): Muestra jugadas, victorias, empates y derrotas
  menu(): Interfaz de navegación por consola
  Las librerias que se utilizaron _ import ramdon
  Función utilizada:
  random.choice(lista)....Devuelve un elemento aleatorio de una lista.
  Funciones básicas de Python (input(), print())
  Estructuras estándar como listas, diccionarios y condicionales (if, elif, else)
  Si ya no deseas jugar aplastas el numeral 4 para salir y basicamente te dara gracias por jugar  
