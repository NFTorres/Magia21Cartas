from Barajas import English_Deck
from Truco_funciones import *
import random

def run():
    """
    The function "run" is the main function of the program, it calls all the other functions and it's
    the one that runs the program.
    """
    line_breaks(2)
    message("¡Buenas! Soy el mago enmascarado\U0001F9D9,\nhoy te mostraré un truco de cartas que te asombrará\U0001F632\n¡El truco de las 21 cartas!")
    line_breaks(3)
    message("Aquí tengo un baraja inglesa\U0001F3F4 con 52 cartas...")
    line_breaks(3)
    show_full_deck(English_Deck)
    line_breaks(3)
    message("Pensándolo bien, la mezclaré un poco ¡Me gusta el desorden!\n")
    message("revolviendo...\U0001F939\n")
    message("una vez más...\U0001F939\n")
    message("¡Listo!")
    line_breaks(3)
    collect_deck = shuffle(English_Deck)
    show_full_deck(collect_deck)
    line_breaks(3)
    message("Ahora seleccionaré 21 cartas aleatoriamente\n")
    selected_deck = random.sample(collect_deck, k=21)
    message("He seleccionado el siguiente mazo: ")
    line_breaks(3)
    show_deck_21_cards(selected_deck)
    line_breaks(3)
    message("Por favor elige una carta, recuerdála muy bien\n")
    message("Si quieres anótala o dícela a un amigo\U0001F4E2\n")
    message("¡Perfecto! Ahora necesito que me digas\n")
    current_deck = selected_deck
    round = 1
    while round <= 3:
        line_breaks(3)
        Q = int(input("¿En cuál columna se encuentra tu carta? (1,2,3): "))
        line_breaks(3)
        if Q == 1:
            message("¡Perfecto! Ahora recogeré las cartas\n")
            message("No te alarmes si tu carta cambia de posición\n")
            message("Recogiendo el mazo...\U0001F939\n")
            message("¡Listo!")
            line_breaks(3)
            current_deck = collect_cards(current_deck, top_column= 1 , middle_column= Q-1, down_column= 2)
            show_deck_21_cards(current_deck)
            round += 1
        elif Q == 2:
            message("¡Perfecto! Ahora recogeré las cartas\n")
            message("No te alarmes si tu carta cambia de posición\n")
            message("Recogiendo el mazo...\U0001F939\n")
            message("¡Listo!")
            line_breaks(3)
            current_deck = collect_cards(current_deck, top_column= 0 , middle_column= Q-1, down_column= 2)
            show_deck_21_cards(current_deck)
            round += 1
        elif Q == 3:
            message("¡Perfecto! Ahora recogeré las cartas\n")
            message("No te alarmes si tu carta cambia de posición\n")
            message("Recogiendo el mazo...\U0001F939\n")
            message("¡Listo!")
            line_breaks(3)
            current_deck = collect_cards(current_deck, top_column= 0 , middle_column = Q-1, down_column = 1)
            show_deck_21_cards(current_deck)
            round += 1
        else:
            message("Columna no reconocida.")
            continue
    line_breaks(3)
    message("¡Perfecto! Ahora recogeré las cartas\n")
    message("Esta vez las mostraré bocabajo\n")
    message("Voy a revelar tu carta\U0001F628\n")
    line_breaks(3)
    message("Tu carta es:\n")
    line_breaks(3)
    reveal_card(current_deck)
    while True:
        success = input("¿He adivinado correctamente?: ")
        if success.lower() == 'si':
            message("¡Qué bien! Sólo me queda despedirme, pero antes recuerda que\n<<Los programadores del mañana son los magos del futuro. Parecerá que tienen poderes mágicos en comparación con los demás>> Gabe Newell \U0001F9D4.\n")
            message("Adios...\U0001F44B\n")
            break
        elif success.lower() == 'no':
            message("¡Chispas...! Disculpame \U0001F648, estoy aprendiendo ¡Pronto lo lograré!\n")
            message("Adios...\U0001F44B\n")
            break
        else:
            success = input("No te entendí correctamente.¿Qué quisiste decir?: ")
            continue
run()

