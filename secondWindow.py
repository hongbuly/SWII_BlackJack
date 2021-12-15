from PyQt5.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from button import Button
from innerCode import *
from gameText import *


class SecondWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("BlackJack Game")
        self.setWindowIcon(QIcon(f"./PNG-cards-1.3/blackjack.png"))
        # setting  the geometry of window
        self.setGeometry(0, 0, 1200, 900)
        self.setStyleSheet("background-color: green")
        self.center()

        self.q_msg_box = QMessageBox()
        self.q_msg_box.setWindowTitle("Result")
        self.q_msg_box.setWindowIcon(QIcon("./PNG-cards-1.3/blackjack.png"))
        self.q_msg_box.setStyleSheet(style_sheet[0])

        self.money = load()
        self.betting_cost = 1000
        # self.dealCount = 0

        self.display = QLabel()
        self.b_display = QLabel('bet: ' + str(self.betting_cost))
        self.b_display.setStyleSheet(style_sheet[1])
        self.m_display = QLabel('money: ' + str(self.money))
        self.m_display.setStyleSheet(style_sheet[2])

        display_vbox = QVBoxLayout()
        display_vbox.addStretch(1)
        display_vbox.addWidget(self.display)
        display_vbox.addWidget(self.b_display)
        display_vbox.addWidget(self.m_display)

        betting_vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addLayout(betting_vbox)

        self.components_btn = list()  # deal, stay, append, reset, plus, minus
        button_groups = [
            {'buttons': ["+100", "-100"], 'layout': betting_vbox},
            {'buttons': ["deal", "new card", "stay", "reset"], 'layout': hbox},
            ]

        for label in button_groups:
            i = 0
            for btnText in label['buttons']:
                self.components_btn.append(Button(btnText, self.button_clicked))
                self.styleButton(self.components_btn[-1])
                label['layout'].addWidget(self.components_btn[-1])
                i += 1

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(display_vbox)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.cntLst = [0, 150, 300, 450, 600, 750]
        self.dLabel = []
        self.pLabel = []
        for _ in range(len(self.cntLst)):
            pl = QLabel(self)
            dl = QLabel(self)
            self.dLabel.append(dl)
            self.pLabel.append(pl)

        # 카드 배치, 베팅 초기화
        self.clear()
        # show all the widgets
        self.show()

    def loadCard(self, label, cardsuit, cnt, num):
        self.pixmap = QPixmap(f"./PNG-cards-1.3/{cardsuit}").scaledToWidth(150)
        label.setPixmap(self.pixmap)
        label.move(cnt, num)  # player 300, dealer 0
        label.resize(self.pixmap.width(), self.pixmap.height())

    # 프로그램 센터에 배치
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clear(self):
        for pl in self.pLabel:
            idx = self.pLabel.index(pl)
            if idx < 2:
                self.loadCard(pl, 'background', self.cntLst[idx], 300)
            else:
                self.loadCard(pl, 'green', self.cntLst[idx], 300)

        for dl in self.dLabel:
            idx = self.dLabel.index(dl)
            if idx < 2:
                self.loadCard(dl, 'background', self.cntLst[idx], 0)
            else:
                self.loadCard(dl, 'green', self.cntLst[idx], 0)

        self.betting_display('', 1000)
        self.components_btn[3].setDisabled(True)
        self.components_btn[4].setDisabled(True)

    def styleButton(self, button):
        button.setCursor(Qt.PointingHandCursor)
        button.setStyleSheet(style_sheet[3])

    def QMessageBoxExec(self, msg):
        msg_box = self.q_msg_box
        msg_box.setText(msg)
        msg_box.exec()
        self.components_btn[3].setDisabled(True)
        self.components_btn[4].setDisabled(True)
        self.components_btn[5].setDisabled(False)
        self.display.setText('If you wanna restart, click reset button')

    def button_clicked(self):
        button = self.sender()
        key = button.text()
        if key == '+100':
            self.betting_display("", self.betting_cost + 100)
        elif key == '-100':
            self.betting_display("", self.betting_cost - 100)
        elif key == 'deal':
            if self.betting_cost < 0:
                self.betting_display("Bet on the positive value.", 1000)
            elif self.betting_cost > 0:
                if self.betting_cost < 1000:
                    self.betting_display("betting min is 1000", 1000)
                elif self.betting_cost > self.money:
                    self.betting_display("You don't have much money", 1000)
                else:
                    self.display.setText("let's start!")
                    self.components_btn[5].setDisabled(True)
                    self.components_disable(False)

                    self.card = set_card()
                    self.intPlayercards = twocard(self.card)
                    # print(self.intPlayercards)
                    # [34, 5]
                    self.intDealercards = twocard(self.card)
                    self.dealercards = intToString_card(self.intDealercards)
                    self.playercards = intToString_card(self.intPlayercards)
                    # print(self.intToString_card)
                    # ['hearts9', 'spades6']
                    self.loadCard(self.pLabel[0], self.playercards[0], self.cntLst[0], 300)
                    self.loadCard(self.pLabel[1], self.playercards[1], self.cntLst[1], 300)
                    self.loadCard(self.dLabel[0], self.dealercards[0], self.cntLst[0], 0)
                    # self.loadDealerCard(self.dLabel[1], self.dealercards[1], self.cntLst[1])

                    if count(self.intPlayercards) == 21:
                        self.money_display(fight_message[3], 3)
            else:
                self.display.setText("Please click betting number")
        elif key == 'new card':
            cardappend(self.intPlayercards, self.card)
            # print(self.intPlayercards)
            # [34, 5, 7]
            self.playercards = intToString_card(self.intPlayercards)
            for pl in self.pLabel:
                idx = self.pLabel.index(pl)
                if idx < len(self.intPlayercards):
                    self.loadCard(pl, self.playercards[idx], self.cntLst[idx], 300)
            res = burst(count(self.intPlayercards))
            if res != 5:
                self.money_display(fight_message[res], res)
        elif key == 'stay':
            self.loadCard(self.dLabel[1], self.dealercards[1], self.cntLst[1], 0)
            # 딜러 카드 합이 17이상이면 더이상 추가 카드를 받을 수 없음
            while count(self.intDealercards) < 17:
                cardappend(self.intDealercards, self.card)
                self.dealercards = intToString_card(self.intDealercards)
                for dl in self.dLabel:
                    idx = self.dLabel.index(dl)
                    if idx < len(self.intDealercards):
                        self.loadCard(dl, self.dealercards[idx], self.cntLst[idx], 0)
            res = fight(count(self.intPlayercards), count(self.intDealercards))
            self.money_display(fight_message[res], res)
        elif key == 'reset':
            self.components_disable(True)
            self.clear()
            self.display.setText('Play more? Click deal button')

    def components_disable(self, check):
        # deal, stay, append, reset, plus, minus
        self.components_btn[3].setDisabled(check)
        self.components_btn[4].setDisabled(check)

        self.components_btn[0].setDisabled(not check)
        self.components_btn[1].setDisabled(not check)
        self.components_btn[2].setDisabled(not check)

    def betting_display(self, message, cost):
        self.display.setText(message)
        self.betting_cost = cost
        self.b_display.setText('bet: ' + str(self.betting_cost))

    def money_display(self, message, num):
        self.QMessageBoxExec(message)
        self.money = set_money(self.money, self.betting_cost, num)
        self.m_display.setText('money: ' + str(self.money))