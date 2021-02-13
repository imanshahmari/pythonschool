""" Playing card library for texas poker game
Author: Iman Shahmari """

version = "1.0"  # Module global variable
from enum import IntEnum
import numpy as np

#Creating super class PlayingCard


class PlayingCard:
    def __init__(self, suit):
        self.suit = suit

    def __lt__(self, other):
        if self.get_value() == other.get_value():
            return self.suit < other.suit
        else:
            return self.get_value() < other.get_value()

    def __eq__(self, other):

        return self.get_value() == other.get_value() and self.suit == other.suit


    def __str__(self):
        return "(" + str(self.__class__) + ',' + str(self.suit) + ',' + str(self.get_value()) + ")"

    def get_value(self):
        """A super class for poker game containing subclasses Numbered,Jack,Queen,King cards

        """
        raise NotImplementedError("missing")

#sub class numbered cards
class NumberedCard(PlayingCard):
    def __init__(self, suit, value):
        super().__init__(suit)
        self.value = value

    def get_value(self):
        return self.value

#sub class Jackcard
class Jackcard(PlayingCard):
    def get_value(self):
        return 11


#sub class QueenCard
class QueenCard(PlayingCard):
    def get_value(self):
        return 12

#sub class KingCard
class KingCard(PlayingCard):
    def get_value(self):
        return 13

#sub class AceCard
class AceCard(PlayingCard):
    def get_value(self):
        return 14

#Creating class for suits
class Suit(IntEnum):
    Clubs = 0
    Diamonds = 1
    Hearts = 2
    Spades = 3


class StandardDeck:
    def __init__(self):
        cards = []
        for i in np.array(range(2, 11)):
            for value, name in enumerate(Suit):
                cards.append(NumberedCard(name, i))
        cards_pic = []
        for value, name in enumerate(Suit):
            cards_pic.append(Jackcard(name))
            cards_pic.append(QueenCard(name))
            cards_pic.append(KingCard(name))
            cards_pic.append(AceCard(name))
        self.cards = cards + cards_pic
    def shuffle(self):
        import random
        return random.shuffle(self.cards)
    def take_card(self):
        mycard = self.cards[0]
        del self.cards[0]
        return mycard


class Hand:
    def __init__(self):
        hand = []
        self.hand = hand
    def add_new_card(self,newcard):
        return self.hand.append(newcard)

    def drop_cards(self,indexes):
        for index in sorted(indexes, reverse = True):
            del self.hand[index]
        return
    def sort_cards(self):
        return self.hand.sort()


class PokerHand:
    def __init__(self,cards_combined):
        self.cards_combined = cards_combined
        self.type =[]
        self.highest_value=[]

    def straight(self):
        # Get rid of repeated values by turning them into sets
        values_cards_combined = [item.get_value() for item in self.cards_combined]
        uniqe_values = list(set(values_cards_combined))
        self.cards_combined.sort()
        self.type = "Straight"

        if len(uniqe_values) == 7:
            list_7_1 = [item.get_value() for item in self.cards_combined[0:5]]
            list_7_2 = [item.get_value() for item in self.cards_combined[1:6]]
            list_7_3 = [item.get_value() for item in self.cards_combined[2:7]]

        elif len(uniqe_values) == 6:
            list_6_1 = [item.get_value() for item in self.cards_combined[0:5]]
            list_6_1.sort()
            self.highest_value = list_6_1[4]
            for i in range(0,4):
                if self.highest_value == 14:
                    if not list_6_1[i] == i+2: self.type = "Not straight"
                else:
                    if not list_6_1[i] + 1 == list_6_1[i+1]: self.type = "Not straight"
            #if self.type == "Straight":
            list_6_2 = [item.get_value() for item in self.cards_combined[1:6]]


        elif len(uniqe_values) == 5:
            list_5 = [item.get_value() for item in self.cards_combined]
            list_5.sort()
            self.highest_value = list_5[4]
            for i in range(0,4):
                if self.highest_value == 14:
                    if not list_5[i] == i+2: self.type = "Not straight"
                else:
                    if not list_5[i] + 1 == list_5[i+1]: self.type = "Not straight"

        elif len(uniqe_values) <=4:
            print("4:e elif")
            self.type = "Not straight"


StandardDeck = StandardDeck()

Hand = Hand()
Hand.add_new_card(StandardDeck.cards[0]) # problem when I put :
Hand.add_new_card(StandardDeck.cards[1]) # problem when I put :


"""
Bordet = []
for i in range(0,5):
    StandardDeck.shuffle()
    Bordet.append(StandardDeck.cards[i])

All = Bordet
All.sort()


Clubs = []
Hearts = []
Diamonds = []
Spades = []
for element in All:
    if element.suit == Suit.Clubs:
        Clubs.append(element)
    elif element.suit == Suit.Hearts:
        Hearts.append(element)
    elif element.suit == Suit.Diamonds:
        Diamonds.append(element)
    elif element.suit == Suit.Spades:
        Spades.append(element)

    print(element.suit)
"""

# Example for a straight card list
List = [StandardDeck.cards[0],StandardDeck.cards[4],StandardDeck.cards[8],StandardDeck.cards[12],StandardDeck.cards[16]]
Pokerhand = PokerHand(List)
Pokerhand.straight()
