'''Este módulo se
'''
__author__ = "Neider Fabian Torres Carvajal"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "nftorres@gmail.com"


import sys, random
from Barajas import *
from time import sleep

# The speed with which the text will be printed on the screen
speed = 0.04



# Aesthetic functions

def line_breaks(num):
    """
    It prints a number of line breaks equal to the number passed to the function
    
    :param num: The number of line breaks you want to print
    """
    for i in range(num-1):
        print("")

def message(message, speed = speed):
    """
    It prints a string one character at a time, with a delay between each character
    
    :param mensaje: The message you want to print
    :param velocidad: The speed of the text
    """
    for i in message:
        print(i, end="")
        sys.stdout.flush()
        sleep(speed)


# Deck handling functions

def shuffle(deck):
    """
    It takes a list of cards from a deck and returns a list of shuffled cards
    
    :param baraja: list of cards
    :return: A list of cards.
    """
    auxiliary = []
    for i in range(len(deck)):
        position = random.randint(1, len(deck))-1
        chosen_card = deck[position]
        auxiliary.append(chosen_card)
        deck.remove(deck[position])
    deck = auxiliary
    return deck

def show_full_deck(deck):
    """
    It prints the cards in the deck, one row at a time, with a slight delay between each card. 
    The cards are dealt in 13 rows and 4 columns.
    
    :param baraja: the deck of cards
    """
    index = 0
    speed = 0.1
    for i in range(0,13):
        for j in range(0,4):
            print(deck[index], end=" ")
            sys.stdout.flush()
            sleep(speed)
            index += 1
        print("")

def show_deck_21_cards(deck):
    """
    It prints the 21 cards of the deck that will be used, one row at a time, with a slight delay between each card.
    The cards are dealt in 7 rows and 3 columns.
    
    :param deck: the deck of cards
    """

    index = 0
    speed = 0.1
    for i in range(0,7):
        for j in range(0,3):
            print(deck[index], end=" ")
            sys.stdout.flush()
            sleep(speed)
            index += 1
        print("")


def collect_cards(deck, top_column, middle_column, down_column):
    """
    It takes a list of cards, and three integers that represent the index of the first card in each
    column, and returns a list of the cards in each column
    
    :param deck: a list of cards
    :param top_column: a index
    :param middle_column: a index
    :param down_column: a index
    :return: A list of cards that are collected from the deck.
    """
    index_list = [top_column, middle_column, down_column]
    collected_cards = []
    for i in index_list:
        increment = i
        for j in deck:
            try:
                collected_cards.append(deck[increment])
                increment += 3
            except:
                pass         
    return collected_cards

def reveal_card(deck):
    """
    It prints the deck of cards, revealing the user's card and hiding the others
    
    :param deck: list of cards
    """
    index = 0
    speed = 0.1
    for i in range(0,7):
        for j in range(0,3):
            if index == 10:
                print(deck[index], end=" ")
                sys.stdout.flush()
                sleep(speed)
                index += 1
            else:
                print('X', end=" ")
                sys.stdout.flush()
                sleep(speed)
                index += 1
        print("")