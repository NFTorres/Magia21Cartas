from Barajas import Baraja_Inglesa
from Truco_funciones import *
import random

def run():
    saltos(2)
    mensaje("¡Buenas!¡Soy Akinator!\U0001F9DE\n¡Encantado de conocerte!\U0001F44B\n¿Sabias que puedo leer tu mente? Aunque no lo creas, soy capaz de penetrar tus neuronas y saber lo que piensas,\nte lo demostraré con el siguiente juego:\n")
    saltos(1)
    mensaje("Descripción del juego:\n")
    mensaje("El juego se llama las 21 cartas, consiste en que yo seleccionaré aleatoriamente 21 cartas\nde una de las barajas que estan disponibles,luego tendrás que pensar en una carta y\ndecirme la columna dónde se encuentra dicha carta, este proceso se repetirá 3 veces y al final revelaré la carta que pensaste.")
    barajar_baraja = barajar(Baraja_Inglesa)
    mazo_seleccionado = random.sample(barajar_baraja, k=21)
    print(mazo_seleccionado)
    print(mostrarmazo(mazo_seleccionado))
    mazo_actual = mazo_seleccionado
    vuelta = 1
    while vuelta <= 3:
        P = int(input("¿En cuál columna se encuentra tu carta? (1,2,3): "))
        if P == 1:
            mazo_actual = recogermazo(mazo_actual, columna_superior= 1 , columna_media = P-1, columna_inferior = 2)
            print(mostrarmazo(mazo_actual))
            vuelta += 1
        elif P == 2:
            mazo_actual = recogermazo(mazo_actual, columna_superior= 0 , columna_media = P-1, columna_inferior = 2)
            print(mostrarmazo(mazo_actual))
            vuelta += 1
        elif P == 3:
            mazo_actual = recogermazo(mazo_actual, columna_superior= 0 , columna_media = P-1, columna_inferior = 1)
            print(mostrarmazo(mazo_actual))
            vuelta += 1
        else:
            print("Columna no reconocida.")
            continue
    print("Tu carta es: ", adivinar(mazo_actual))
run()

