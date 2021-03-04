from cardlib import *
deck = StandardDeck()
deck.shuffle()


class Model():
    def __init__(self):
        self.deck = deck
        self.pot = 0
        self.pot_before = 0
        self.pot_after = 0
        self.strange = "sadasdasdas"
       #self.active_player = active_player


    # string with name of players
class Player():
    def __init__(self, model,player_name):
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


    def call(self,model):
        call_sum = model.pot_after - model.pot_before
        self.money = self.money - call_sum
        model.pot = model.pot + call_sum

    def fold(self,model,player):
        model.victory = "Spelaren som inte foldade vann"
        player.money = player.money + model.pot


class Table():
    hand= Hand()
    hand.add_new_card(deck.take_card())
    hand.add_new_card(deck.take_card())
    hand.add_new_card(deck.take_card())


Game = Model()
player1 = Player(Game,"K90")
player2 = Player(Game,"Han")
player1.bet(Game,100)
player2.call(Game)
player2.fold(Game, player1)
Table = Table()


