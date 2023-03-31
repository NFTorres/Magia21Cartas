'''Este módulo se
'''
__author__ = "Neider Fabian Torres Carvajal"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "nftorres@gmail.com"


import sys, random
from Barajas import *
from time import sleep

velocidad = 0.04

# Métodos estéticos y de espera de respuesta



# Métodos estéticos

def saltos(num):
    for i in range(num-1):
        print("")

def mensaje(mensaje, velocidad = velocidad):
    for i in mensaje:
        print(i, end="")
        sys.stdout.flush()
        sleep(velocidad)

# Métodos de manipulación de barajas y mazos

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
    indice = 0
    velocidad = 0.1
    for i in range(0,13):
        for j in range(0,4):
            print(baraja[indice], end=" ")
            sys.stdout.flush()
            sleep(velocidad)
            indice += 1
        print("")

def mostrarmazo(baraja):

    indice = 0
    velocidad = 0.1
    for i in range(0,7):
        for j in range(0,3):
            print(baraja[indice], end=" ")
            sys.stdout.flush()
            sleep(velocidad)
            indice += 1
        print("")


def recogermazo(baraja, columna_superior, columna_media, columna_inferior):
    
    index_list = [columna_superior, columna_media, columna_inferior]
    mazo_recogido = []
    for i in index_list:
        incremento = i
        for j in baraja:
            try:
                mazo_recogido.append(baraja[incremento])
                incremento += 3
            except:
                pass         
    return mazo_recogido

def adivinar(baraja):
    indice = 0
    velocidad = 0.1
    for i in range(0,7):
        for j in range(0,3):
            if indice == 10:
                print(baraja[indice], end=" ")
                sys.stdout.flush()
                sleep(velocidad)
                indice += 1
            else:
                print('X', end=" ")
                sys.stdout.flush()
                sleep(velocidad)
                indice += 1
        print("")