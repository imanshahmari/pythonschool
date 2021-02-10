from cardlib import *
import numpy as np

card1 = Jackcard(Suit.Diamonds)
print(card1.suit)
x = card1.get_value()
cards=[]
for i in np.array(range(2,11)):
    for value,name in enumerate(Suit):
        cards.append(NumberedCard(i,name))
cards_pic=[]
for value, name in enumerate(Suit):
    cards_pic.append(Jackcard(name))
    cards_pic.append(QueenCard(name))
    cards_pic.append(KingCard(name))
    cards_pic.append(AceCard(name))
cards = cards + cards_pic
