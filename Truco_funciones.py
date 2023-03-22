import os
import random
from Barajas import *

def clear():
    os.system("clear")

def barajar(baraja):
    auxiliar = []
    for i in range(len(baraja)):
        posicion = random.randint(1, len(baraja))-1
        carta_elegida = baraja[posicion]
        auxiliar.append(carta_elegida)
        baraja.remove(baraja[posicion])
    baraja = auxiliar
    return baraja

def mostrarbaraja(baraja):
    
    for fila in range(5):
        for columna in range(10):
            for carta in baraja[fila][columna]:
                ancho = 3
                largo = 2

                esp = " "
                for i in range(0, ancho):
                    esp = esp + "-"
                for j in range(0, largo):
                    esp = esp + "\n|"
                    for k in range(0, ancho):
                        if k == 1:
                            esp = esp + carta
                            continue
                        else:
                            esp = esp + " "
                    esp = esp + "|"
                esp = esp + "\n "
                for u in range(0,ancho):
                    esp = esp + "-"
                print(esp)

mostrarbaraja(Baraja_Inglesa)