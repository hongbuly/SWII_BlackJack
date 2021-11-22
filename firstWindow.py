from PyQt5.QtGui import *
from musicPlayer import *


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
        self.volumeUpButton = QPushButton("+", clicked=self.music.volumeUp)
        self.volumeDownButton = QPushButton("-", clicked=self.music.volumeDown)
        self.volumeMuteButton = QPushButton("Mute", clicked=self.music.volumeMute)

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
