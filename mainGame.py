from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtMultimedia import *

from innerCode import *

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

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()

    def volumeUp(self):
        currentVolume = self.player.volume() #
        print(currentVolume)
        self.player.setVolume(currentVolume + 5)

    def volumeDown(self):
        currentVolume = self.player.volume() #
        print(currentVolume)
        self.player.setVolume(currentVolume - 5)

    def volumeMute(self):
        self.player.setMuted(not self.player.isMuted())

    def playAudioFile(self):
        full_file_path = os.path.join(os.getcwd(), './sounds/bgm.mp3')
        url = QtCore.QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()


class FirstWindow(QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BlackJack Game")
        self.setWindowIcon(QIcon("./PNG-cards-1.3/blackjack.png"))
        self.setGeometry(0, 0, 900, 600)
        self.setStyleSheet('background-color: green')

        self.music = MusicPlayer()
        self.music.playAudioFile()

        self.image = QPixmap("./PNG-cards-1.3/title.png")
        self.label = QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setPixmap(self.image)

        self.startbutton = QPushButton("PLAY")
        self.volumeUpButton = QPushButton("+",clicked=self.music.volumeUp)
        self.volumeDownButton = QPushButton("-",clicked=self.music.volumeDown)
        self.volumeMuteButton = QPushButton("Mute",clicked=self.music.volumeMute)

        self.styleButton(self.volumeUpButton)
        self.styleButton(self.volumeDownButton)
        self.styleButton(self.volumeMuteButton)

        self.volumelayout = QHBoxLayout()
        self.volumelayout.addWidget(self.volumeDownButton)
        self.volumelayout.addWidget(self.volumeMuteButton)
        self.volumelayout.addWidget(self.volumeUpButton)

        self.startbutton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.startbutton.setStyleSheet(
            """QPushButton{background-color: rgb(249, 228, 183);
            color: black;
            border-radius: 25px;
            font-family: 'Georgia';
            font-size: 40px;
            margin-bottom: 5px;
            padding: 8px 0;}"""
            """QPushButton::hover
            {
            background-color : white;
            }
            """
        )

        self.startbutton.clicked.connect(self.secondwindow)
        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.grid.addWidget(self.startbutton, 2, 1)
        self.grid.addLayout(self.volumelayout, 3, 1)
        self.setLayout(self.grid)

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def secondwindow(self):
        self.switch_window.emit()

    def styleButton(self, button):
        button.setCursor(QtCore.Qt.PointingHandCursor)
        button.setStyleSheet(
            """QPushButton{background-color: rgb(249, 228, 183);
                        color: black;
                        border-radius: 15px;
                        font-family: 'Georgia';
                        font-size: 25px;
                        padding: 5px 0;}"""
            """QPushButton::hover
            {
            background-color : white;
            }
            """
        )

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def styleButton(self, button):
        button.setCursor(QtCore.Qt.PointingHandCursor)
        button.setStyleSheet(
            """QPushButton{background-color: rgb(249, 228, 183);
                        color: black;
                        border-radius: 15px;
                        font-family: 'Georgia';
                        font-size: 25px;;
                        padding: 5px 0;}"""
            """QPushButton::hover
            {
            background-color : white;
            }
            """
        )

    def firstwindow(self):
        self.switch_window.emit()



class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BlackJack Game")
        self.setWindowIcon(QIcon(f"./PNG-cards-1.3/blackjack.png"))
        # setting  the geometry of window
        self.setGeometry(0, 0, 1200, 900)
        self.setStyleSheet("background-color: green")
        self.center()

        self.qmsgBox = QMessageBox()
        self.qmsgBox.setWindowTitle("Result")
        self.qmsgBox.setWindowIcon(QIcon("./PNG-cards-1.3/blackjack.png"))
        self.qmsgBox.setStyleSheet(
            """QMessageBox
            {
            background-color: white;
            font-family: 'Georgia';
            }
            """
        )

        self.money = load()
        self.betting_cost = 1000
        self.dealCount = 0

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
        stayBtn = Button("stay", self.button_clicked)
        appendBtn = Button("new card", self.button_clicked)
        resetBtn = Button("reset", self.button_clicked)
        self.pbetBtn = Button("+100", self.button_clicked)
        self.mbetBtn = Button("-100", self.button_clicked)

        self.styleButton(self.dealBtn)
        self.styleButton(stayBtn)
        self.styleButton(appendBtn)
        self.styleButton(resetBtn)
        self.styleButton(self.pbetBtn)
        self.styleButton(self.mbetBtn)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.pbetBtn)
        vbox1.addWidget(self.mbetBtn)

        vbox2 = QVBoxLayout()
        vbox2.addStretch(1)
        vbox2.addWidget(self.display)
        vbox2.addWidget(self.b_display)
        vbox2.addWidget(self.m_display)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addWidget(self.dealBtn)
        hbox.addWidget(stayBtn)
        hbox.addWidget(appendBtn)
        hbox.addWidget(resetBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(vbox2)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.cntLst = [0,150,300,450,600,750]
        self.pl1 = QLabel(self)
        self.pl2 = QLabel(self)
        self.pl3 = QLabel(self)
        self.pl4 = QLabel(self)
        self.pl5 = QLabel(self)
        self.pl6 = QLabel(self)
        self.pLabel = [self.pl1,self.pl2,self.pl3,self.pl4,self.pl5, self.pl6]

        self.dl1 = QLabel(self)
        self.dl2 = QLabel(self)
        self.dl3 = QLabel(self)
        self.dl4 = QLabel(self)
        self.dl5 = QLabel(self)
        self.dl6 = QLabel(self)
        self.dLabel = [self.dl1,self.dl2,self.dl3,self.dl4,self.dl5, self.dl6]

        for pl in self.pLabel:
            idx = self.pLabel.index(pl)
            if idx == 0 or idx == 1:
                self.loadPPlayerCard(pl, 'background', self.cntLst[idx])
            else:
                self.loadPPlayerCard(pl,'green', self.cntLst[idx])
            # print(self.pLabel.index(pl))

        for dl in self.dLabel:
            idx = self.dLabel.index(dl)
            if idx == 0 or idx == 1:
                self.loadDDealerCard(dl,'background', self.cntLst[idx])
            else:
                self.loadDDealerCard(dl, 'green', self.cntLst[idx])


        # show all the widgets
        self.show()


    def loadPPlayerCard(self, label, cardsuit, cnt):
        self.pixmap = QPixmap(f"./PNG-cards-1.3/{cardsuit}").scaledToWidth(150)
        label.setPixmap(self.pixmap)
        label.move(cnt,300)
        label.resize(self.pixmap.width(),self.pixmap.height())
        # print('pWidth: ' + str(self.pixmap.width()) + ', pHeight: ' + str(self.pixmap.height()))
        # pWidth: 150, pHeight: 214
        #    :
        # pWidth: 150, pHeight: 227

    def loadDDealerCard(self, label, cardsuit, cnt):
        self.pixmap = QPixmap(f"./PNG-cards-1.3/{cardsuit}").scaledToWidth(150)
        label.setPixmap(self.pixmap)
        label.move(cnt,0)
        label.resize(self.pixmap.width(),self.pixmap.height())
        # print('dWidth: ' + str(self.pixmap.width() + ', dHeight: ' + str(self.pixmap.height()))
        # dWidth: 150, dHeight: 214
        #    :
        # dWidth: 150, dHeight: 227


    # 프로그램 센터에 배치
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 카드 배치, 베팅 초기화
    def clear(self):
        for pl in self.pLabel:
            idx = self.pLabel.index(pl)
            if idx < 2:
                self.loadPPlayerCard(pl, 'background', self.cntLst[idx])
            else:
                self.loadPPlayerCard(pl, 'green', self.cntLst[idx])

        for dl in self.dLabel:
            idx = self.dLabel.index(dl)
            if idx < 2:
                self.loadDDealerCard(dl, 'background', self.cntLst[idx])
            else:
                self.loadDDealerCard(dl, 'green', self.cntLst[idx])

        self.betting_cost = 1000
        self.b_display.setText('bet: ' + str(self.betting_cost))

    def styleButton(self, button):
        button.setCursor(QtCore.Qt.PointingHandCursor)
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

    def button_clicked(self):
        button = self.sender()
        key = button.text()
        if key == '+100':
            self.betting_cost += 100
            self.b_display.setText('bet: '+ str(self.betting_cost))
            # self.m_display.setText('money: ' + str(self.money))
        elif key == '-100':
            self.betting_cost -= 100
            self.b_display.setText('bet: ' + str(self.betting_cost))
            # self.m_display.setText('money: ' + str(self.money))
        elif key == 'deal':
            if self.dealCount > 1:
                self.qmsgBox.setText("Please click reset button")
                self.qmsgBox.exec()
                return
            self.dealCount = 1
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
                    self.pbetBtn.setDisabled(True)
                    self.mbetBtn.setDisabled(True)
                    self.dealBtn.setDisabled(True)
                    self.display.setText("let's start!")

                    self.card = set_card()
                    self.intPlayercards = twocard(self.card)
                    # print(self.intPlayercards)
                    # [34, 5]
                    self.intDealercards = twocard(self.card)
                    self.dealercards = intToString_card(self.intDealercards)
                    self.playercards = intToString_card(self.intPlayercards)
                    # print(self.intToString_card)
                    # ['hearts9', 'spades6']
                    self.loadPPlayerCard(self.pl1, self.playercards[0], self.cntLst[self.pLabel.index(self.pl1)])
                    self.loadPPlayerCard(self.pl2, self.playercards[1], self.cntLst[self.pLabel.index(self.pl2)])
                    self.loadDDealerCard(self.dl1, self.dealercards[0], self.cntLst[self.dLabel.index(self.dl1)])
                    # self.loadDDealerCard(self.dl2, self.dealercards[1], self.cntLst[self.dLabel.index(self.dl2)])

                    # 시작하자마자 burst 불가능
                    # if burst(count(self.intPlayercards)):
                    #     print("lose")
                    #     QMessageBox.about(self, "BlackJack", "you lose !")
                    #     return
                    if count(self.intPlayercards) == 21:
                        self.qmsgBox.setText("Congratulations! \nBlack Jack!")
                        self.qmsgBox.exec()
                        self.dealCount+=1
                        self.money = set_money(self.money, self.betting_cost, 3)
                        self.m_display.setText('money: ' + str(self.money))
                    return
            else:
                self.display.setText("Please click betting number")
                return

        elif key == 'new card':
            if self.dealCount == 0:
                self.qmsgBox.setText("You should click deal button first")
                self.qmsgBox.exec()
                return
            if self.dealCount > 1:
                self.qmsgBox.setText("Please click reset button")
                self.qmsgBox.exec()
                return
            cardappend(self.intPlayercards, self.card)
            # print(self.intPlayercards)
            # [34, 5, 7]
            self.playercards = intToString_card(self.intPlayercards)
            for pl in self.pLabel:
                idx = self.pLabel.index(pl)
                if idx < len(self.intPlayercards):
                    self.loadPPlayerCard(pl, self.playercards[idx], self.cntLst[idx])
            if burst(count(self.intPlayercards)):
                self.qmsgBox.setText("Burst!")
                self.qmsgBox.exec()
                self.dealCount += 1
                self.money = set_money(self.money, self.betting_cost, 0)
                self.m_display.setText('money: ' + str(self.money))
                return
            elif count(self.intPlayercards) == 21:
                self.qmsgBox.setText("Congratulations! \nBlack Jack!")
                self.qmsgBox.exec()
                self.dealCount += 1
                self.money = set_money(self.money, self.betting_cost, 3)
                self.m_display.setText('money: ' + str(self.money))
                return
            else:
                return

        elif key == 'stay':
            if self.dealCount == 0:
                self.qmsgBox.setText("You should click deal button first")
                self.qmsgBox.exec()
                return
            if self.dealCount > 1:
                self.qmsgBox.setText("Please click reset button")
                self.qmsgBox.exec()
                return
            self.loadDDealerCard(self.dl2, self.dealercards[1], self.cntLst[self.dLabel.index(self.dl2)])
            # player의 burst 메소드 이용
            if burst(count(self.intDealercards)):
                self.qmsgBox.setText("you win!")
                self.qmsgBox.exec()
                self.dealCount += 1
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
                            self.loadDDealerCard(dl, self.dealercards[idx], self.cntLst[idx])
                if burst(count(self.intDealercards)):
                    self.qmsgBox.setText("You Win!")
                    self.qmsgBox.exec()
                    self.dealCount += 1
                    self.money = set_money(self.money, self.betting_cost, 3)
                    self.m_display.setText('money: ' + str(self.money))
                    return
                elif count(self.intDealercards) == 21:
                    self.qmsgBox.setText("You lose!")
                    self.qmsgBox.exec()
                    self.dealCount += 1
                    self.money = set_money(self.money, self.betting_cost, 0)
                    self.m_display.setText('money: ' + str(self.money))
                    return
                else:
                    res = fight(count(self.intPlayercards),count(self.intDealercards))
                    if res == 2:
                        self.qmsgBox.setText("Draw!")
                        self.qmsgBox.exec()
                        self.dealCount += 1
                        self.money = set_money(self.money, self.betting_cost, 2)
                        self.m_display.setText('money: ' + str(self.money))
                        return
                    elif res == 1:
                        self.qmsgBox.setText("You win!")
                        self.qmsgBox.exec()
                        self.dealCount += 1
                        self.money = set_money(self.money, self.betting_cost, 3)
                        self.m_display.setText('money: ' + str(self.money))
                        return
                    else:
                        self.qmsgBox.setText("You lose!")
                        self.qmsgBox.exec()
                        self.dealCount += 1
                        self.money = set_money(self.money, self.betting_cost, 0)
                        self.m_display.setText('money: ' + str(self.money))
                        return

        # if key == 'reset':
        else:
            if self.dealCount == 0:
                self.qmsgBox.setText("You should click deal button first")
                self.qmsgBox.exec()
                return
            self.dealBtn.setDisabled(False)
            self.pbetBtn.setDisabled(False)
            self.mbetBtn.setDisabled(False)
            self.dealCount = 0
            for pl in self.pLabel:
                idx = self.pLabel.index(pl)
                if idx < 2:
                    self.loadPPlayerCard(pl, 'background', self.cntLst[idx])
                else:
                    self.loadPPlayerCard(pl, 'green', self.cntLst[idx])

            for dl in self.dLabel:
                idx = self.dLabel.index(dl)
                if idx < 2:
                    self.loadDDealerCard(dl, 'background', self.cntLst[idx])
                else:
                    self.loadDDealerCard(dl, 'green', self.cntLst[idx])

            self.betting_cost = 1000
            self.b_display.setText('bet: ' + str(self.betting_cost))

class Controller:
    def __init__(self):
        pass

    def show_firstWindow(self):
        self.firstwindow = FirstWindow()
        self.firstwindow.switch_window.connect(self.show_secondWindow)
        self.firstwindow.show()

    def show_secondWindow(self):
        self.firstwindow.close()
        self.window = SecondWindow()
        self.window.close()
        self.window.show()


if __name__ == "__main__":
    import sys, os
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_firstWindow()
    sys.exit(app.exec_())