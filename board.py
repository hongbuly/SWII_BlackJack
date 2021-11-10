from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from functions import *


class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Board(QWidget):
    card = []
    player = []
    dealer = []

    def __init__(self, parent=None):
        super().__init__(parent)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        button_layout = QGridLayout()
        start_button = Button("start", self.buttonClicked)
        push_button = Button("push", self.buttonClicked)
        end_button = Button("end", self.buttonClicked)
        button_layout.addWidget(start_button, 0, 1)
        button_layout.addWidget(push_button, 0, 2)
        button_layout.addWidget(end_button, 0, 3)

        main_layout = QGridLayout()
        main_layout.setSizeConstraint(QLayout.SetFixedSize)
        main_layout.addWidget(self.display, 0, 0, 1, 2)
        main_layout.addLayout(button_layout, 1, 0)

        self.setLayout(main_layout)
        self.setWindowTitle("Black Jack")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == 'start':
            self.card = set_card()
            print(self.card)
            self.player.clear()
            self.dealer.clear()

            for i in range(2):
                self.player.append(self.card.pop(0))
                self.dealer.append(self.card.pop(0))
            print(self.player)
            print(show_card(self.player))
            self.display.setText(show_card(self.player))
        elif key == 'push':
            self.player.append(self.card.pop())
            self.display.setText(show_card(self.player))
        elif key == 'end':
            player_result = count(self.player)
            dealer_result = count(self.dealer)
            if player_result > 21 and dealer_result > 21:
                self.display.setText("Draw")
            elif player_result > 21 and dealer_result <= 21:
                self.display.setText("Lose")
            elif player_result <= 21 and dealer_result > 21:
                self.display.setText("Win")
            elif player_result <= 21 and dealer_result <= 21:
                if player_result < dealer_result:
                    self.display.setText("Lose")
                elif player_result > dealer_result:
                    self.display.setText("Win")
                elif player_result == dealer_result:
                    self.display.setText("Draw")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    board = Board()
    board.show()
    sys.exit(app.exec_())