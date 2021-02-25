from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


qt_app = QApplication(sys.argv)



class PlayerWidget(QWidget):
    def __init__(self,label):
        super().__init__()

        self.label = label
        hbox = QHBoxLayout()

        playerButton = QPushButton(label)

        hbox.addWidget(playerButton)
        self.setLayout(hbox)



class Buttons(QWidget):

    def __init__(self,labels):
        super().__init__()  # Call the QWidget initialization as well!

        self.labels = labels
        hbox = QHBoxLayout()

        for label in labels:
            button = QPushButton(label)
            hbox.addWidget(button)

        """callButton = QPushButton("Call")
        betButton = QPushButton("Bet")
        foldButton = QPushButton("Fold")
        hbox = QHBoxLayout()
        hbox.addWidget(callButton)
        hbox.addWidget(betButton)
        hbox.addWidget(foldButton)"""

        self.setLayout(hbox)




class CardDisplay(QWidget):
    def __init__(self,label):
        super().__init__()
        self.label = label

        vbox = QVBoxLayout()
        CARDS = QPushButton(label)
        vbox.addWidget(CARDS)

        self.setLayout(vbox)




class WholeWindow(QGroupBox):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout()

        hbox.addWidget(PlayerWidget('Player 1'))
        hbox.addWidget(PlayerWidget('Player 2'))
        hbox.addWidget(Buttons(['Call', 'Bet', 'Fold']))

        vbox = QVBoxLayout()
        vbox.addWidget(CardDisplay('CARDS PLACEHOLDER'))
        vbox.addLayout(hbox)



        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Poker Game (LGBTQ Friendly)')
        self.setWindowIcon(QIcon("1280px-Gay_Pride_Flag.svg.png"))



stylesheet = """
    WholeWindow {
        background-image: url("greenback.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    } """


qt_app.setStyleSheet(stylesheet)


win = WholeWindow()
win.show()
qt_app.exec_()