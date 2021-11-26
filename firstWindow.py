from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QGridLayout, QDesktopWidget
from musicPlayer import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from gameText import style_sheet


def styleButton(button):
    button.setCursor(Qt.PointingHandCursor)
    button.setStyleSheet(style_sheet[4])


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
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(self.image)

        self.start_button = QPushButton("PLAY")
        self.volumeUpButton = QPushButton("+")
        self.volumeUpButton.clicked.connect(self.music.volumeUp)
        self.volumeDownButton = QPushButton("-")
        self.volumeDownButton.clicked.connect(self.music.volumeDown)
        self.volumeMuteButton = QPushButton("Mute")
        self.volumeMuteButton.clicked.connect(self.music.volumeMute)

        styleButton(self.volumeUpButton)
        styleButton(self.volumeDownButton)
        styleButton(self.volumeMuteButton)

        self.volume_layout = QHBoxLayout()
        self.volume_layout.addWidget(self.volumeDownButton)
        self.volume_layout.addWidget(self.volumeMuteButton)
        self.volume_layout.addWidget(self.volumeUpButton)

        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_button.setStyleSheet(style_sheet[5])

        self.start_button.clicked.connect(self.secondWindowEmit)
        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.grid.addWidget(self.start_button, 2, 1)
        self.grid.addLayout(self.volume_layout, 3, 1)
        self.setLayout(self.grid)

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def secondWindowEmit(self):
        self.switch_window.emit()
