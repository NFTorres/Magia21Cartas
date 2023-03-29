import os
import random
from Barajas import *

def clear():
    os.system("clear")

def saltos(num):
    for i in range(num-1):
        print()
def mensaje(mensaje):
    print(mensaje)

def barajar(baraja):
    auxiliar = []
    for i in range(len(baraja)):
        posicion = random.randint(1, len(baraja))-1
        carta_elegida = baraja[posicion]
        auxiliar.append(carta_elegida)
        baraja.remove(baraja[posicion])
    baraja = auxiliar
    return baraja

def mostrarmazo(baraja):

    indice = 0
    for i in range(0,7):
        for j in range(0,3):
            print(baraja[indice], end="  ")
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
    print(mazo_recogido)
    return mazo_recogido

def adivinar(baraja):
    return baraja[10]