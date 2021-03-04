from cardlib import *
deck = StandardDeck()
deck.shuffle()




class Model():
    def __init__(self,players,table):
        self.deck = deck
        self.pot = 0
        self.pot_before = 0
        self.pot_after = 0
        self.players = players
        self.active_player = 0
        self.table = table
        self.bet_sum = 0

    def call(self):
        call_sum = self.pot_after - self.pot_before
        print(call_sum)
        self.pot = self.pot + call_sum
        self.players[self.active_player].call(call_sum)
        self.active_player = (self.active_player + 1) % 2


    def bet(self): #,bet_sum som input från gui
        bet_sum = int(input("Enter bet sum:"))

        self.bet_sum = self.bet_sum + bet_sum
        self.pot_before = self.pot
        self.pot = self.pot + bet_sum
        self.pot_after=self.pot
        self.players[self.active_player].bet(bet_sum)
        self.active_player = (self.active_player + 1) % 2


    def fold(self):
        #model.victory = "Spelaren som inte foldade vann"
        self.active_player = (self.active_player + 1) % 2




    # string with name of players
class Player():
    def __init__(self,player_name):
        super().__init__()
        self.player_name = player_name
        self.cards = [deck.take_card(),deck.take_card()]
        self.money = 500

    def bet(self, model,bet_sum):
        self.bet_sum = 0
        self.bet_sum = self.bet_sum + bet_sum
        model.pot_before=model.pot
        model.pot = model.pot + bet_sum
        model.pot_after=model.pot
        self.money = self.money - bet_sum

    def call(self,call_sum):
        self.money = self.money - call_sum



    def fold(self,player):
        #model.victory = "Spelaren som inte foldade vann"
        self.money = player.money + self.pot


class Table():
    hand= Hand()
    hand.add_new_card(deck.take_card())
    hand.add_new_card(deck.take_card())
    hand.add_new_card(deck.take_card())



player1 = Player("K90")
player2 = Player("Han")
table = Table()
Game = Model([player1, player2],table)



