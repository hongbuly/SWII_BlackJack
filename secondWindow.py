from PyQt5.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt
from button import Button
from innerCode import *


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
        self.q_msg_box.setStyleSheet(
            """QMessageBox
            {
            background-color: white;
            font-family: 'Georgia';
            }
            """
        )

        self.money = load()
        self.betting_cost = 1000
        # self.dealCount = 0

        self.display = QLabel()
        self.b_display = QLabel('bet: ' + str(self.betting_cost))
        self.b_display.setStyleSheet(
            """QLabel

            {
            font-size: 18px;
            font-family: 'Georgia';
            color: blue;
            }
            """
        )
        self.m_display = QLabel('money: ' + str(self.money))
        self.m_display.setStyleSheet(
            """QLabel
            {
            font-size: 18px;
            font-family: 'Georgia';
            color: blue;
            }
            """
        )

        self.dealBtn = Button("deal", self.button_clicked)
        self.stayBtn = Button("stay", self.button_clicked)
        self.appendBtn = Button("new card", self.button_clicked)
        self.resetBtn = Button("reset", self.button_clicked)
        self.plusBetBtn = Button("+100", self.button_clicked)
        self.minusBetBtn = Button("-100", self.button_clicked)

        self.styleButton(self.dealBtn)
        self.styleButton(self.stayBtn)
        self.styleButton(self.appendBtn)
        self.styleButton(self.resetBtn)
        self.styleButton(self.plusBetBtn)
        self.styleButton(self.minusBetBtn)

        betting_vbox = QVBoxLayout()
        betting_vbox.addWidget(self.plusBetBtn)
        betting_vbox.addWidget(self.minusBetBtn)

        display_vbox = QVBoxLayout()
        display_vbox.addStretch(1)
        display_vbox.addWidget(self.display)
        display_vbox.addWidget(self.b_display)
        display_vbox.addWidget(self.m_display)

        hbox = QHBoxLayout()
        hbox.addLayout(betting_vbox)
        hbox.addWidget(self.dealBtn)
        hbox.addWidget(self.stayBtn)
        hbox.addWidget(self.appendBtn)
        hbox.addWidget(self.resetBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(display_vbox)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # self.pl1 = QLabel(self)
        # self.pl2 = QLabel(self)
        # self.pl3 = QLabel(self)
        # self.pl4 = QLabel(self)
        # self.pl5 = QLabel(self)
        # self.pl6 = QLabel(self)
        # self.pLabel = [self.pl1, self.pl2, self.pl3, self.pl4, self.pl5, self.pl6]
        #
        # self.dl1 = QLabel(self)
        # self.dl2 = QLabel(self)
        # self.dl3 = QLabel(self)
        # self.dl4 = QLabel(self)
        # self.dl5 = QLabel(self)
        # self.dl6 = QLabel(self)
        # self.dLabel = [self.dl1, self.dl2, self.dl3, self.dl4, self.dl5, self.dl6]
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

    def loadPlayerCard(self, label, cardsuit, cnt):
        self.pixmap = QPixmap(f"./PNG-cards-1.3/{cardsuit}").scaledToWidth(150)
        label.setPixmap(self.pixmap)
        label.move(cnt,300)
        label.resize(self.pixmap.width(),self.pixmap.height())

    def loadDealerCard(self, label, cardsuit, cnt):
        self.pixmap = QPixmap(f"./PNG-cards-1.3/{cardsuit}").scaledToWidth(150)
        label.setPixmap(self.pixmap)
        label.move(cnt,0)
        label.resize(self.pixmap.width(),self.pixmap.height())

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
                self.loadPlayerCard(pl, 'background', self.cntLst[idx])
            else:
                self.loadPlayerCard(pl, 'green', self.cntLst[idx])

        for dl in self.dLabel:
            idx = self.dLabel.index(dl)
            if idx < 2:
                self.loadDealerCard(dl, 'background', self.cntLst[idx])
            else:
                self.loadDealerCard(dl, 'green', self.cntLst[idx])

        self.betting_cost = 1000
        self.display.setText('')
        self.b_display.setText('bet: ' + str(self.betting_cost))
        self.stayBtn.setDisabled(True)
        self.appendBtn.setDisabled(True)

    def styleButton(self, button):
        button.setCursor(Qt.PointingHandCursor)
        button.setStyleSheet(
            """QToolButton{background-color: rgb(249, 228, 183);
            color: black;
            border-radius: 5px;
            font-family: 'Georgia';
            font-size: 20px;
            }"""
            """QToolButton::hover
            {
            background-color: white;
            }
            """
        )

    def QMessageBoxExec(self, msg):
        msg_box = self.q_msg_box
        msg_box.setText(msg)
        msg_box.exec()
        self.appendBtn.setDisabled(True)
        self.stayBtn.setDisabled(True)
        self.display.setText('If you wanna restart, click reset button')

    def button_clicked(self):
        button = self.sender()
        key = button.text()
        if key == '+100':
            self.betting_cost += 100
            self.b_display.setText('bet: ' + str(self.betting_cost))
        elif key == '-100':
            self.betting_cost -= 100
            self.b_display.setText('bet: ' + str(self.betting_cost))
        elif key == 'deal':
            if self.betting_cost < 0:
                self.display.setText("Bet on the positive value.")
                self.betting_cost = 1000
                self.b_display.setText('bet: ' + str(self.betting_cost))
                return
            elif self.betting_cost > 0:
                if self.betting_cost < 1000:
                    self.display.setText("betting min is 1000")
                    self.betting_cost = 1000
                    self.b_display.setText('bet: ' + str(self.betting_cost))
                    return
                elif self.betting_cost > self.money:
                    self.display.setText("You don't have much money")
                    self.betting_cost = 1000
                    self.b_display.setText('bet: ' + str(self.betting_cost))
                    return
                else:
                    self.display.setText("let's start!")
                    self.stayBtn.setDisabled(False)
                    self.appendBtn.setDisabled(False)
                    self.plusBetBtn.setDisabled(True)
                    self.minusBetBtn.setDisabled(True)
                    self.dealBtn.setDisabled(True)

                    self.card = set_card()
                    self.intPlayercards = twocard(self.card)
                    # print(self.intPlayercards)
                    # [34, 5]
                    self.intDealercards = twocard(self.card)
                    self.dealercards = intToString_card(self.intDealercards)
                    self.playercards = intToString_card(self.intPlayercards)
                    # print(self.intToString_card)
                    # ['hearts9', 'spades6']
                    self.loadPlayerCard(self.pLabel[0], self.playercards[0], self.cntLst[0])
                    self.loadPlayerCard(self.pLabel[1], self.playercards[1], self.cntLst[1])
                    self.loadDealerCard(self.dLabel[0], self.dealercards[0], self.cntLst[0])
                    # self.loadDealerCard(self.dLabel[1], self.dealercards[1], self.cntLst[1])

                    if count(self.intPlayercards) == 21:
                        self.QMessageBoxExec("Congratulations! \nBlack Jack!")
                        self.money = set_money(self.money, self.betting_cost, 3)
                        self.m_display.setText('money: ' + str(self.money))
                    return
            else:
                self.display.setText("Please click betting number")
                return

        elif key == 'new card':
            cardappend(self.intPlayercards, self.card)
            # print(self.intPlayercards)
            # [34, 5, 7]
            self.playercards = intToString_card(self.intPlayercards)
            for pl in self.pLabel:
                idx = self.pLabel.index(pl)
                if idx < len(self.intPlayercards):
                    self.loadPlayerCard(pl, self.playercards[idx], self.cntLst[idx])
            if burst(count(self.intPlayercards)):
                self.QMessageBoxExec("Burst!")
                self.money = set_money(self.money, self.betting_cost, 0)
                self.m_display.setText('money: ' + str(self.money))
            elif count(self.intPlayercards) == 21:
                self.QMessageBoxExec("Congratulations! \nBlack Jack!")
                self.money = set_money(self.money, self.betting_cost, 3)
                self.m_display.setText('money: ' + str(self.money))
            else:
                return

        elif key == 'stay':
            self.loadDealerCard(self.dLabel[1], self.dealercards[1], self.cntLst[1])
            if count(self.intDealercards) > 21:
                self.QMessageBoxExec("you win!")

                self.money = set_money(self.money, self.betting_cost, 1)
                self.m_display.setText('money: ' + str(self.money))
                return
            else:
                # 딜러 카드 합이 17이상이면 더이상 추가 카드를 받을 수 없음
                while count(self.intDealercards) < 17:
                    cardappend(self.intDealercards, self.card)
                    self.dealercards = intToString_card(self.intDealercards)
                    for dl in self.dLabel:
                        idx = self.dLabel.index(dl)
                        if idx < len(self.intDealercards):
                            self.loadDealerCard(dl, self.dealercards[idx], self.cntLst[idx])
                if count(self.intDealercards) > 21:
                    self.QMessageBoxExec("you win!")
                    self.money = set_money(self.money, self.betting_cost, 3)
                    self.m_display.setText('money: ' + str(self.money))
                    return
                elif count(self.intDealercards) == 21:
                    self.QMessageBoxExec("You lose!")
                    self.money = set_money(self.money, self.betting_cost, 0)
                    self.m_display.setText('money: ' + str(self.money))
                    return
                else:
                    res = fight(count(self.intPlayercards), count(self.intDealercards))
                    if res == 2:
                        self.QMessageBoxExec("Draw!")
                        self.money = set_money(self.money, self.betting_cost, 2)
                        self.m_display.setText('money: ' + str(self.money))
                        return
                    elif res == 1:
                        self.QMessageBoxExec("You win!")
                        self.money = set_money(self.money, self.betting_cost, 3)
                        self.m_display.setText('money: ' + str(self.money))
                        return
                    else:
                        self.QMessageBoxExec("You lose!")
                        self.money = set_money(self.money, self.betting_cost, 0)
                        self.m_display.setText('money: ' + str(self.money))
                        return

        # if key == 'reset':
        else:
            self.stayBtn.setDisabled(True)
            self.appendBtn.setDisabled(True)
            self.dealBtn.setDisabled(False)
            self.plusBetBtn.setDisabled(False)
            self.minusBetBtn.setDisabled(False)
            self.clear()
            self.display.setText('Play more? Click deal button')
            return