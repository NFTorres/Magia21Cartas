from Barajas import Baraja_Inglesa
from Truco_funciones import *
import random

def run():
    saltos(2)
    mensaje("¡Buenas! Soy el mago enmascarado\U0001F9D9,\nhoy te mostraré un truco de cartas que te asombrará\U0001F632\n¡El truco de las 21 cartas!")
    saltos(3)
    mensaje("Aquí tengo un baraja inglesa\U0001F3F4 con 52 cartas...")
    saltos(3)
    mostrarbaraja(Baraja_Inglesa)
    saltos(3)
    mensaje("Pensándolo bien, la mezclaré un poco ¡Me gusta el desorden!\n")
    mensaje("revolviendo...\U0001F939\n")
    mensaje("una vez más...\U0001F939\n")
    mensaje("¡Listo!")
    saltos(3)
    baraja_mezclada = barajar(Baraja_Inglesa)
    mostrarbaraja(baraja_mezclada)
    saltos(3)
    mensaje("Ahora seleccionaré 21 cartas aleatoriamente\n")
    mazo_seleccionado = random.sample(baraja_mezclada, k=21)
    mensaje("He seleccionado el siguiente mazo: ")
    saltos(3)
    mostrarmazo(mazo_seleccionado)
    saltos(3)
    mensaje("Por favor elige una carta, recuerdála muy bien\n")
    mensaje("Si quieres anótala o dícela a un amigo\U0001F4E2\n")
    mensaje("¡Perfecto! Ahora necesito que me digas\n")
    mazo_actual = mazo_seleccionado
    vuelta = 1
    while vuelta <= 3:
        saltos(3)
        P = int(input("¿En cuál columna se encuentra tu carta? (1,2,3): "))
        saltos(3)
        if P == 1:
            mensaje("¡Perfecto! Ahora recogeré las cartas\n")
            mensaje("No te alarmes si tu carta cambia de posición\n")
            mensaje("Recogiendo el mazo...\U0001F939\n")
            mensaje("¡Listo!")
            saltos(3)
            mazo_actual = recogermazo(mazo_actual, columna_superior= 1 , columna_media = P-1, columna_inferior = 2)
            mostrarmazo(mazo_actual)
            vuelta += 1
        elif P == 2:
            mensaje("¡Perfecto! Ahora recogeré las cartas\n")
            mensaje("No te alarmes si tu carta cambia de posición\n")
            mensaje("Recogiendo el mazo...\U0001F939\n")
            mensaje("¡Listo!")
            saltos(3)
            mazo_actual = recogermazo(mazo_actual, columna_superior= 0 , columna_media = P-1, columna_inferior = 2)
            mostrarmazo(mazo_actual)
            vuelta += 1
        elif P == 3:
            mensaje("¡Perfecto! Ahora recogeré las cartas\n")
            mensaje("No te alarmes si tu carta cambia de posición\n")
            mensaje("Recogiendo el mazo...\U0001F939\n")
            mensaje("¡Listo!")
            saltos(3)
            mazo_actual = recogermazo(mazo_actual, columna_superior= 0 , columna_media = P-1, columna_inferior = 1)
            mostrarmazo(mazo_actual)
            vuelta += 1
        else:
            mensaje("Columna no reconocida.")
            continue
    saltos(3)
    mensaje("¡Perfecto! Ahora recogeré las cartas\n")
    mensaje("Esta vez las mostraré bocabajo\n")
    mensaje("Voy a revelar tu carta\U0001F628\n")
    saltos(3)
    mensaje("Tu carta es:\n")
    saltos(3)
    adivinar(mazo_actual)
    while True:
        acierto = input("¿He adivinado correctamente?: ")
        if acierto.lower() == 'si':
            mensaje("¡Qué bien! Sólo me queda despedirme, pero antes recuerda que\n<<Los programadores del mañana son los magos del futuro. Parecerá que tienen poderes mágicos en comparación con los demás>> Gabe Newell \U0001F9D4.\n")
            mensaje("Adios...\U0001F44B\n")
            break
        elif acierto.lower() == 'no':
            mensaje("¡Chispas...! Disculpame \U0001F648, estoy aprendiendo ¡Pronto lo lograré!\n")
            mensaje("Adios...\U0001F44B\n")
            break
        else:
            acierto = input("No te entendí correctamente.¿Qué quisiste decir?: ")
            continue
run()

