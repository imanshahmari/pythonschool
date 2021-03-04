from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from modelkristofer import *

qt_app = QApplication(sys.argv)



class PlayerWidget(QWidget):
    def __init__(self,label,money ):
        super().__init__()

        self.label = label
        self.money = money
        hbox = QHBoxLayout()

        player_label = QLabel(label)
        player_money = QLabel(money)

        hbox.addWidget(player_label)

        vbox = QVBoxLayout()
        vbox.addWidget(player_money)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


class Buttons(QWidget):

    def __init__(self,model):
        super().__init__()  # Call the QWidget initialization as well!

        call = QPushButton("call")
        bet = QPushButton("Bet")
        fold = QPushButton("Fold")

        call.clicked.connect(model.call)
        bet.clicked.connect(model.bet)
        #fold.clicked.connect(model.fold)

        hbox = QHBoxLayout()

        hbox.addWidget(call)
        hbox.addWidget(bet)
        hbox.addWidget(fold)





        self.setLayout(hbox)




class CardDisplay(QWidget):
    def __init__(self,label):
        super().__init__()
        self.label = label
        str_cards = [c.__str__() for c in Table.hand.cards]
        vbox = QVBoxLayout()
        CARDS = QLabel(str(str_cards))
        vbox.addWidget(CARDS)

        self.setLayout(vbox)




class WholeWindow(QGroupBox):
    def __init__(self,model):  #skicka in model

        super().__init__()
        hbox = QHBoxLayout()


        hbox.addWidget(PlayerWidget("Player stash: " + str(player1.money),"Player name : " + player1.player_name))
        hbox.addWidget(PlayerWidget("Player stash: " + str(player2.money),"Player name : " + player2.player_name))
        hbox.addWidget(Buttons(model))
        hbox.addWidget(QLabel("Pot: " + str(model.pot)))

        vbox = QVBoxLayout()
        vbox.addWidget(CardDisplay('CARDS PLACEHOLDER'))

        vbox.addLayout(hbox)



        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Poker Game (LGBTQ Friendly)')
        self.setWindowIcon(QIcon("1280px-Gay_Pride_Flag.svg.png"))



stylesheet = """
    WholeWindow {
        background-image: url("gree.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    } """


qt_app.setStyleSheet(stylesheet)

win = WholeWindow(Game)
win.show()
qt_app.exec_()