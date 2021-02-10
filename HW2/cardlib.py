""" Playing card library for texas poker game
Author: Iman Shahmari """

version = "1.0"  # Module global variable
from enum import Enum
import numpy as np

#Creating super class PlayingCard
class PlayingCard():
    def get_value(self):
        """A super class for poker game containing subclasses Numbered,Jack,Queen,King cards

        """
        raise NotImplementedError("missing")
#sub class numbered cards
class NumberedCard(PlayingCard):
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    def get_value(self):
        return self.value

#sub class Jackcard
class Jackcard(PlayingCard):
    def __init__(self,suit):
        self.suit = suit
    def get_value(self):
        return 11


#sub class QueenCard
class QueenCard(PlayingCard):
    def __init__(self,suit):
        self.suit = suit
    def get_value(self):
        return 12

#sub class KingCard
class KingCard(PlayingCard):
    def __init__(self,suit):
        self.suit = suit
    def get_value(self):
        return 13

#sub class AceCard
class AceCard(PlayingCard):
    def __init__(self,suit):
        self.suit = suit
    def get_value(self):
        return 14

#Creating class for suits
class Suit(Enum):
    Clubs = 0
    Diamonds = 1
    Hearts = 2
    Spades = 3


class StandardDeck:
    def __init__(self):
        cards = []
        for i in np.array(range(2, 11)):
            for value, name in enumerate(Suit):
                cards.append(NumberedCard(i, name))
        cards_pic = []
        for value, name in enumerate(Suit):
            cards_pic.append(Jackcard(name))
            cards_pic.append(QueenCard(name))
            cards_pic.append(KingCard(name))
            cards_pic.append(AceCard(name))
        cards = cards + cards_pic