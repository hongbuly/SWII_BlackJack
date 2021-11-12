from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton, QLabel
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from inner import *


class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 50)
        size.setWidth(max(size.width(), size.height()))
        return size


class Board(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.card = []
        self.player = []
        self.dealer = []
        self.money = load()
        self.betting_cost = 0

        # 화면 3개(딜러, 플레이어, 돈)
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setMaxLength(50)
        self.display1 = QLineEdit()
        self.display1.setReadOnly(True)
        self.display1.setMaxLength(50)
        self.money_display = QLineEdit()
        self.money_display.setReadOnly(True)
        self.money_display.setMaxLength(50)

        button_layout = QGridLayout()
        start_button = Button("start", self.button_clicked)
        push_button = Button("push", self.button_clicked)
        end_button = Button("end", self.button_clicked)
        button_layout.addWidget(start_button, 0, 1)
        button_layout.addWidget(push_button, 0, 2)
        button_layout.addWidget(end_button, 0, 3)

        betting_layout = QGridLayout()
        betting_label = QLabel("betting")
        self.betting_display = QLineEdit()
        self.betting_display.setMaxLength(50)
        betting_layout.addWidget(betting_label, 0, 1)
        betting_layout.addWidget(self.betting_display, 0, 2)

        main_layout = QGridLayout()
        main_layout.setSizeConstraint(QLayout.SetFixedSize)
        main_layout.addWidget(self.display1, 0, 0, 1, 2)
        main_layout.addWidget(self.display, 1, 0, 1, 2)
        main_layout.addWidget(self.money_display, 3, 0, 1, 2)
        main_layout.addLayout(betting_layout, 4, 0)
        main_layout.addLayout(button_layout, 2, 0)

        self.setLayout(main_layout)
        self.setWindowTitle("Black Jack")
        self.money_display.setText('Money:' + str(self.money))

    def button_clicked(self):
        button = self.sender()
        key = button.text()
        if key == 'start':
            betting_cost = self.betting_display.text()
            if betting_cost.isdigit() and betting_cost:
                self.betting_cost = int(betting_cost)
                if self.betting_cost < 1000:
                    self.display.setText("Betting min : 1000")
                    return

                if self.betting_cost > self.money:
                    self.display.setText("You don't have much money")
                    return

                self.betting_display.setReadOnly(True)
            else:
                self.display.setText("Write betting number")
                return

            # 매 게임마다 카드 리셋후, 카드 지급, 내부와 외부 분리
            self.card = set_card()
            self.player = twocard(self.card)
            self.dealer = twocard(self.card)
            # print Gui 에서 안보임
            print('player')
            print(show_card(self.player))
            print('dealer')
            print(show_card(self.dealer))
            self.display.setText('player:' + show_card(self.player))
            self.display1.setText('dealer:' + show_card(self.dealer[1:]) + 'H')

        elif key == 'push':
            # 카드를 받지 않은 상태에서 push 버튼 클릭시 문구 추가, 내부와 외부 분리
            cardappend(self.player, self.card)
            self.display.setText('player:' + show_card(self.player))
            print(show_card(self.player))
            if count(self.player) > 21:
                player_result = count(self.player)
                dealer_result = count(self.dealer)
                self.display.setText(fight(player_result, dealer_result))

        elif key == 'end':
            # 딜러 알고리즘 추가
            dealer_algo(count(self.dealer), self.dealer, self.card)
            self.display1.setText('dealer:' + show_card(self.dealer))
            # 플레이어와 딜러 숫자합 비교, 내부와 외부 분리
            player_result = count(self.player)
            dealer_result = count(self.dealer)
            fight_num = fight(player_result, dealer_result)
            self.display.setText(get_fight_text(fight_num))
            self.money = set_money(self.money, self.betting_cost, fight_num)
            self.player.clear()
            self.dealer.clear()

            print(player_result, dealer_result)

            self.betting_display.setReadOnly(False)
            self.money_display.setText('Money:' + str(self.money))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    board = Board()
    board.show()
    sys.exit(app.exec_())
